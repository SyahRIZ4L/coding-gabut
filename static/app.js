const state = {
  questions: [],
  choices: [],
  current: 0,
  gender: null,
};

const welcome = document.querySelector('#welcome');
const quiz = document.querySelector('#quiz');
const loading = document.querySelector('#loading');
const result = document.querySelector('#result');
const questionNumber = document.querySelector('#questionNumber');
const questionText = document.querySelector('#questionText');
const progressText = document.querySelector('#progressText');
const progressBar = document.querySelector('#progressBar');
const answerGrid = document.querySelector('#answerGrid');
const nextButton = document.querySelector('#nextButton');
const backButton = document.querySelector('#backButton');
const statusText = document.querySelector('#statusText');

async function loadQuestions() {
  const response = await fetch('/api/questions');
  state.questions = await response.json();
  state.choices = Array(state.questions.length).fill(null);
}

function showView(view) {
  [welcome, quiz, loading, result].forEach((section) => section.classList.add('hidden'));
  view.classList.remove('hidden');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderQuestion() {
  const question = state.questions[state.current];
  const number = String(state.current + 1).padStart(2, '0');
  questionNumber.textContent = `Pertanyaan ${number}`;
  progressText.textContent = `${number} / ${state.questions.length}`;
  progressBar.style.width = `${((state.current + 1) / state.questions.length) * 100}%`;
  questionText.textContent = question.text;
  answerGrid.innerHTML = '';

  question.options.forEach((option, index) => {
    const button = document.createElement('button');
    button.className = 'answer-card';
    button.type = 'button';
    button.setAttribute('aria-label', option);
    button.title = option;
    button.setAttribute('aria-pressed', state.choices[state.current] === index ? 'true' : 'false');
    button.innerHTML = `<span class="answer-index">${index + 1}</span>`;
    if (state.choices[state.current] === index) button.classList.add('selected');
    button.addEventListener('click', () => {
      state.choices[state.current] = index;
      answerGrid.querySelectorAll('.answer-card').forEach((card) => {
        card.classList.remove('selected');
        card.setAttribute('aria-pressed', 'false');
      });
      button.classList.add('selected');
      button.setAttribute('aria-pressed', 'true');

      if (state.current === state.questions.length - 1) {
        showResults();
        return;
      }

      state.current += 1;
      statusText.textContent = `QUESTION ${String(state.current + 1).padStart(2, '0')} / 40`;
      renderQuestion();
    });
    answerGrid.appendChild(button);
  });

  backButton.disabled = state.current === 0;
  backButton.style.opacity = state.current === 0 ? '.35' : '1';
  nextButton.disabled = state.choices[state.current] === null;
  nextButton.innerHTML = state.current === state.questions.length - 1 ? 'Lihat hasil <span>→</span>' : 'Berikutnya <span>→</span>';
}

function characterImage(name) {
  const slug = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  return `/static/PA/${slug}.png`;
}

function renderMatch(match, index) {
  const rank = String(index + 1).padStart(2, '0');
  const winnerClass = index === 0 ? ' winner-match' : '';
  const image = characterImage(match.name);
  const artwork = index === 0 ? `<div class="character-image"><img src="${image}" alt="Ilustrasi ${match.name}" loading="lazy"><span class="avatar-fallback">${match.name.charAt(0)}</span></div>` : '';
  return `
    <article class="match-card${winnerClass}">
      <div class="match-visual">
        <div class="match-rank">${rank}</div>
        ${artwork}
      </div>
      <div class="match-info"><span class="match-label">${index === 0 ? 'RESONANSI TERKUAT' : `MATCH 0${index + 1}`}</span><h3 class="match-name">${match.name}</h3><div class="match-score">MATCH SCORE / ${match.score}%</div><div class="match-traits">${match.traits}</div></div>
      <p class="match-description">${match.analysis}</p>
    </article>
  `;
}

function renderSameGenderNote(match) {
  const note = document.querySelector('#sameGenderNote');
  if (!match) {
    note.classList.add('hidden');
    note.innerHTML = '';
    return;
  }

  note.innerHTML = `<span class="section-label">KECOCOKAN SESAMA GENDER</span><p>Kalau kamu ingin melihat karakter ${match.gender}, kecocokan tertinggimu adalah <strong>${match.name}</strong> dengan skor <strong>${match.score}%</strong>.</p>`;
  note.classList.remove('hidden');
}

async function showResults() {
  showView(loading);
  statusText.textContent = 'ANALYZING RESONANCE';
  const response = await fetch('/api/result', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ gender: state.gender, choices: state.choices }),
  });
  const data = await response.json();
  if (!response.ok) {
    window.alert(data.error || 'Terjadi kesalahan.');
    showView(quiz);
    return;
  }

  document.querySelector('#traitGrid').innerHTML = data.traits.map((trait) => `
    <article class="trait-card">
      <div class="trait-card-head"><h3>${trait.name}</h3><span>${trait.score > 0 ? '+' : ''}${trait.score}</span></div>
      <div class="trait-meter"><i style="width: ${Math.max(8, ((trait.score + 12) / 24) * 100)}%"></i></div>
      <p class="trait-overview">${trait.overview}</p>
      <p><strong>Kekuatan:</strong> ${trait.strength}.</p>
      <p><strong>Terlihat saat:</strong> ${trait.signals}</p>
      <p class="trait-balance"><strong>Penjaga keseimbangan:</strong> ${trait.balance}</p>
    </article>
  `).join('');

  document.querySelector('#matchList').innerHTML = data.matches.map(renderMatch).join('');
  renderSameGenderNote(data.same_gender_match);
  setupShareCard(data.matches[0]);
  document.querySelectorAll('.character-image img').forEach((image) => {
    image.addEventListener('error', () => {
      image.closest('.character-image').classList.add('image-missing');
    }, { once: true });
  });
  statusText.textContent = 'REPORT READY';
  showView(result);
}

function setupShareCard(match) {
  const shareButton = document.querySelector('#shareButton');
  const shareOverlay = document.querySelector('#shareCard');
  const shareContent = document.querySelector('#shareContent');
  const closeButton = document.querySelector('#closeShareButton');
  const copyButton = document.querySelector('#copyShareButton');
  const copyStatus = document.querySelector('#copyStatus');
  if (!match) return;

  shareContent.innerHTML = `<div class="share-character"><img src="${characterImage(match.name)}" alt="Ilustrasi ${match.name}"><span>${match.name}</span></div><strong class="share-score">${match.score}%</strong><p>${match.traits}</p>`;
  const summary = `Saya paling beresonansi dengan ${match.name} (${match.score}%). Trait yang paling dekat: ${match.traits}.`;
  shareButton.onclick = () => shareOverlay.classList.remove('hidden');
  closeButton.onclick = () => shareOverlay.classList.add('hidden');
  shareOverlay.onclick = (event) => {
    if (event.target === shareOverlay) shareOverlay.classList.add('hidden');
  };
  copyButton.onclick = async () => {
    await navigator.clipboard.writeText(summary);
    copyStatus.textContent = 'Ringkasan berhasil disalin.';
  };
}

document.querySelectorAll('.gender-card').forEach((button) => {
  button.addEventListener('click', async () => {
    state.gender = button.dataset.gender;
    await loadQuestions();
    state.current = 0;
    statusText.textContent = 'QUESTION 01 / 40';
    showView(quiz);
    renderQuestion();
  });
});

nextButton.addEventListener('click', () => {
  if (state.current === state.questions.length - 1) {
    showResults();
    return;
  }
  state.current += 1;
  statusText.textContent = `QUESTION ${String(state.current + 1).padStart(2, '0')} / 40`;
  renderQuestion();
});

backButton.addEventListener('click', () => {
  if (state.current > 0) {
    state.current -= 1;
    renderQuestion();
  }
});

document.querySelector('#restartButton').addEventListener('click', () => {
  state.questions = [];
  state.choices = [];
  state.current = 0;
  state.gender = null;
  statusText.textContent = 'PERSONALITY INDEX';
  showView(welcome);
});

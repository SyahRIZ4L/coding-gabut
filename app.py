from flask import Flask, jsonify, render_template, request

import test as quiz


app = Flask(__name__)

LIKERT_OPTIONS = [
    "Sangat setuju",
    "Setuju",
    "Agak setuju",
    "Netral",
    "Agak tidak setuju",
    "Tidak setuju",
    "Sangat tidak setuju",
]

LIKERT_VALUES = (3, 2, 1, 0, -1, -2, -3)

RELATIONSHIP_PROFILES = {
    "sahabat": {
        "label": "Sahabat",
        "description": "Karakter yang paling cocok menjadi teman dekat dan tempat berbagi cerita.",
        "core": {"sosial": 1.4, "empati": 1.4, "humoris": 1.2},
        "support": {"tenang": 1.0, "spontan": 0.9, "berani": 0.6},
        "complement": {"mandiri": 0.5, "logis": 0.4},
        "conflicts": {"ambisius": 0.2, "disiplin": 0.2},
    },
    "pacar": {
        "label": "Pacar",
        "description": "Karakter yang berpotensi punya chemistry romantis paling kuat denganmu.",
        "gender": "opposite",
        "core": {"empati": 1.5, "sosial": 1.2, "humoris": 1.0},
        "support": {"berani": 0.9, "spontan": 0.8, "mandiri": 0.7},
        "complement": {"tenang": 0.6, "logis": 0.4},
        "conflicts": {"ambisius": 0.3, "disiplin": 0.2},
    },
    "pasangan_hidup": {
        "label": "Pasangan hidup",
        "description": "Karakter yang paling cocok membangun hubungan serius dan saling menopang.",
        "gender": "opposite",
        "core": {"empati": 1.5, "tenang": 1.3, "disiplin": 1.2},
        "support": {"mandiri": 1.0, "logis": 0.8, "berani": 0.6},
        "complement": {"sosial": 0.5, "humoris": 0.4},
        "conflicts": {"spontan": 0.3, "ambisius": 0.2},
    },
}

LIKERT_QUESTIONS = [
    ("Saat situasi memanas, saya bisa menunda reaksi sampai memahami apa yang sebenarnya terjadi.", "tenang"),
    ("Ketika banyak masalah datang sekaligus, saya mampu memilih satu hal untuk ditangani lebih dulu.", "tenang"),
    ("Saya tetap dapat berpikir jernih meskipun orang di sekitar saya sedang panik.", "tenang"),
    ("Saya membutuhkan waktu hening untuk mengembalikan keseimbangan setelah hari yang berat.", "tenang"),
    ("Saya bersedia mengambil langkah pertama meskipun belum ada jaminan hasilnya.", "berani"),
    ("Ketika melihat perlakuan tidak adil, saya sulit berpura-pura tidak melihatnya.", "berani"),
    ("Saya lebih memilih mencoba lalu belajar daripada terus menunggu kondisi sempurna.", "berani"),
    ("Saat rencana gagal, saya mencari langkah berikutnya sebelum menyalahkan keadaan.", "berani"),
    ("Saya ingin memahami alasan di balik sebuah aturan, keputusan, atau pendapat.", "logis"),
    ("Ketika menerima informasi baru, saya membedakan fakta, asumsi, dan opini.", "logis"),
    ("Sebelum memilih, saya membandingkan konsekuensi jangka pendek dan jangka panjang.", "logis"),
    ("Saya menikmati memecah masalah rumit menjadi bagian-bagian yang bisa dikerjakan.", "logis"),
    ("Saya dapat menangkap perubahan kecil pada suasana hati orang yang dekat dengan saya.", "empati"),
    ("Sebelum memberi nasihat, saya berusaha memahami apa yang sebenarnya dibutuhkan orang itu.", "empati"),
    ("Saya tetap peduli pada dampak keputusan saya meskipun tidak ada yang mengawasinya.", "empati"),
    ("Saya sering menyadari kebutuhan orang lain bahkan sebelum mereka memintanya.", "empati"),
    ("Ketika menghadapi masalah, saya biasanya mencoba mencari jalan keluar sebelum meminta bantuan.", "mandiri"),
    ("Saya dapat mengambil keputusan tanpa harus mendapat persetujuan semua orang.", "mandiri"),
    ("Saya nyaman memiliki cara kerja dan ruang pribadi yang saya atur sendiri.", "mandiri"),
    ("Saya tetap merasa bertanggung jawab atas pilihan saya meskipun hasilnya tidak sesuai harapan.", "mandiri"),
    ("Jika rencana berubah mendadak, saya dapat menemukan pendekatan baru dengan cepat.", "spontan"),
    ("Saya tertarik mencoba sesuatu hanya karena ada kemungkinan pengalaman baru di dalamnya.", "spontan"),
    ("Saya dapat memanfaatkan kesempatan yang muncul tanpa persiapan panjang.", "spontan"),
    ("Saya lebih mudah bersemangat ketika ada variasi daripada rutinitas yang sama setiap hari.", "spontan"),
    ("Saya memecah pekerjaan besar menjadi langkah kecil agar benar-benar selesai.", "disiplin"),
    ("Orang lain dapat mengandalkan saya untuk menepati kesepakatan yang sudah dibuat.", "disiplin"),
    ("Saya tetap menyelesaikan kewajiban meskipun tidak sedang merasa termotivasi.", "disiplin"),
    ("Saya merasa lebih tenang ketika jadwal, barang, dan tanggung jawab saya tertata.", "disiplin"),
    ("Saya biasanya menemukan cara alami untuk memulai percakapan dengan orang baru.", "sosial"),
    ("Setelah berinteraksi dengan orang yang tepat, energi saya sering terasa bertambah.", "sosial"),
    ("Dalam kelompok, saya berusaha memastikan tidak ada orang yang merasa diabaikan.", "sosial"),
    ("Saya menikmati berbagi ide, cerita, atau pengalaman untuk membangun kedekatan.", "sosial"),
    ("Saya menetapkan target yang membuat kemampuan saya terus berkembang.", "ambisius"),
    ("Saya merasa puas ketika berhasil mencapai sesuatu yang sebelumnya tampak sulit.", "ambisius"),
    ("Saya bersedia berlatih lebih lama jika itu mendekatkan saya pada hasil yang diinginkan.", "ambisius"),
    ("Saya sering membayangkan versi masa depan yang ingin saya bangun secara konkret.", "ambisius"),
    ("Saya tahu kapan candaan dapat membantu orang merasa lebih nyaman.", "humoris"),
    ("Dalam situasi sulit, saya sering menemukan sudut pandang yang membuat beban terasa lebih ringan.", "humoris"),
    ("Saya dapat membuat orang tertawa tanpa meremehkan perasaan mereka.", "humoris"),
    ("Saya menggunakan humor untuk membuka percakapan yang awalnya terasa canggung.", "humoris"),
]

NEGATIVE_QUESTION_IDS = {
    6, 10, 15, 19, 23, 27, 31, 35,
}


def serialize_questions():
    return [
        {
            "id": index,
            "text": question,
            "trait": trait,
            "options": LIKERT_OPTIONS,
            "negative": index in NEGATIVE_QUESTION_IDS,
        }
        for index, (question, trait) in enumerate(LIKERT_QUESTIONS)
    ]


def calculate_result(gender, choices):
    scores = {trait: 0 for _, trait in LIKERT_QUESTIONS}

    for question_index, option_index in enumerate(choices):
        trait = LIKERT_QUESTIONS[question_index][1]
        value = LIKERT_VALUES[int(option_index)]
        if question_index in NEGATIVE_QUESTION_IDS:
            value *= -1
        scores[trait] += value

    matches = find_likert_matches(scores)[:3]
    top_traits = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:3]
    relationships = {
        relationship: [
            serialize_match(match)
            for match in find_relationship_matches(scores, gender, relationship)[:3]
        ]
        for relationship in RELATIONSHIP_PROFILES
    }
    trait_reading = [
        {
            "name": quiz.TRAIT_DETAILS.get(trait, {}).get("label", trait),
            "score": score,
            "overview": quiz.TRAIT_DETAILS.get(trait, {}).get("overview", "Trait yang cukup menonjol dalam pola jawabanmu."),
            "strength": quiz.TRAIT_DETAILS.get(trait, {}).get("strength", "Trait utama dalam jawabanmu."),
            "signals": quiz.TRAIT_DETAILS.get(trait, {}).get("signals", "Terlihat dalam cara kamu merespons situasi sehari-hari."),
            "balance": quiz.TRAIT_DETAILS.get(trait, {}).get("balance", "Jaga agar trait ini tetap seimbang."),
        }
        for trait, score in top_traits
    ]

    return {
        "traits": trait_reading,
        "matches": [serialize_match(match) for match in matches],
        "relationships": relationships,
    }


def find_likert_matches(scores):
    return find_matches_for_gender(scores)


def find_matches_for_gender(scores, target_gender=None):
    max_score = 12
    matches = []
    for name, profile in quiz.CHARACTER_PROFILES.items():
        if target_gender and profile.get("gender") != target_gender:
            continue
        similarity = sum(
            max(0, min(1, (scores.get(trait, 0) + max_score) / (max_score * 2))) * value
            for trait, value in profile.get("traits", {}).items()
        )
        profile_total = sum(profile.get("traits", {}).values()) or 1
        matches.append((similarity / profile_total * 100, name, profile))
    return sorted(matches, reverse=True)


def find_relationship_matches(scores, gender, relationship):
    relationship_profile = RELATIONSHIP_PROFILES[relationship]
    target_gender = None
    if relationship_profile.get("gender") == "opposite":
        target_gender = "laki-laki" if gender == "perempuan" else "perempuan"
    matches = []

    for name, profile in quiz.CHARACTER_PROFILES.items():
        if target_gender and profile.get("gender") != target_gender:
            continue
        character_traits = profile.get("traits", {})
        core_score = weighted_trait_score(scores, character_traits, relationship_profile["core"], "similar")
        support_score = weighted_trait_score(scores, character_traits, relationship_profile["support"], "similar")
        complement_score = weighted_trait_score(scores, character_traits, relationship_profile["complement"], "complement")
        conflict_penalty = weighted_trait_score(scores, character_traits, relationship_profile["conflicts"], "conflict")
        score = max(0, min(100, (core_score * 0.5) + (support_score * 0.25) + (complement_score * 0.15) - (conflict_penalty * 0.1)))
        reason = build_relationship_reason(scores, character_traits, relationship_profile)
        matches.append((score, name, profile, reason))

    return sorted(matches, reverse=True)


def weighted_trait_score(user_scores, character_traits, weights, mode):
    total = sum(weights.values()) or 1
    score = 0
    for trait, weight in weights.items():
        user_value = (user_scores.get(trait, 0) + 12) / 24
        character_value = character_traits.get(trait, 0) / 5
        if mode == "complement":
            difference = abs(user_value - character_value)
            trait_score = 1 - min(1, abs(difference - 0.35) / 0.35)
        elif mode == "conflict":
            trait_score = abs(user_value - character_value)
        else:
            trait_score = 1 - abs(user_value - character_value)
        score += max(0, min(1, trait_score)) * weight
    return score / total * 100


def build_relationship_reason(scores, character_traits, relationship_profile):
    core_traits = relationship_profile["core"]
    strongest = sorted(
        core_traits,
        key=lambda trait: (
            1 - abs(
                (scores.get(trait, 0) + 12) / 24
                - character_traits.get(trait, 0) / 5
            )
        ),
        reverse=True,
    )[:2]
    labels = [quiz.TRAIT_DETAILS.get(trait, {}).get("label", trait) for trait in strongest]
    return f"Kuat di {', '.join(labels)}."


def serialize_match(match):
    similarity, name, profile = match[:3]
    return {
        "name": name,
        "score": round(similarity, 1),
        "gender": profile.get("gender"),
        "traits": quiz.explain_traits(profile.get("traits", {}), 4),
        "analysis": quiz.build_profile_analysis(profile),
        "reason": match[3] if len(match) > 3 else None,
    }


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/questions")
def questions():
    return jsonify(serialize_questions())


@app.post("/api/result")
def result():
    payload = request.get_json(silent=True) or {}
    gender = payload.get("gender")
    choices = payload.get("choices")

    if gender not in {"laki-laki", "perempuan"}:
        return jsonify({"error": "Gender tidak valid."}), 400
    if not isinstance(choices, list) or len(choices) != len(LIKERT_QUESTIONS):
        return jsonify({"error": "Semua pertanyaan harus dijawab."}), 400
    if any(not isinstance(choice, int) or choice not in range(7) for choice in choices):
        return jsonify({"error": "Pilihan jawaban tidak valid."}), 400

    return jsonify(calculate_result(gender, choices))


if __name__ == "__main__":
    app.run(debug=True, port=5000)

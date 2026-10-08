from dataclasses import dataclass


@dataclass
class Answer:
	text: str
	traits: dict[str, int]


CHARACTER_PROFILES = {
	"March 7th": {"gender": "perempuan", "traits": {"sosial": 5, "humoris": 5, "berani": 4, "empati": 4}, "description": "Ceria, ekspresif, ingin tahu, dan sangat menghargai teman."},
	"Himeko": {"gender": "perempuan", "traits": {"tenang": 5, "logis": 4, "empati": 4, "ambisius": 3}, "description": "Dewasa, bijaksana, bertanggung jawab, dan suka memimpin perjalanan."},
	"Bronya": {"gender": "perempuan", "traits": {"disiplin": 5, "tenang": 4, "empati": 4, "ambisius": 4}, "description": "Pemimpin yang serius, beretika, strategis, dan rela berkorban."},
	"Seele": {"gender": "perempuan", "traits": {"berani": 5, "mandiri": 5, "empati": 3, "spontan": 3}, "description": "Tegas, impulsif, mandiri, dan sangat membela orang yang lemah."},
	"Kafka": {"gender": "perempuan", "traits": {"tenang": 5, "logis": 4, "mandiri": 4, "berani": 4}, "description": "Tenang, misterius, manipulatif, percaya diri, dan sulit ditebak."},
	"Silver Wolf": {"gender": "perempuan", "traits": {"logis": 5, "humoris": 4, "mandiri": 4, "spontan": 3}, "description": "Jenius teknologi yang santai, suka bermain, dan menganggap hidup sebagai game."},
	"Fu Xuan": {"gender": "perempuan", "traits": {"logis": 5, "ambisius": 4, "tenang": 4, "disiplin": 4}, "description": "Percaya diri, analitis, perfeksionis, dan yakin pada perhitungannya."},
	"Qingque": {"gender": "perempuan", "traits": {"humoris": 5, "spontan": 4, "mandiri": 3, "sosial": 3}, "description": "Santai, cerdas tetapi pemalas, dan selalu mencari cara termudah."},
	"Tingyun": {"gender": "perempuan", "traits": {"sosial": 5, "logis": 4, "humoris": 3, "mandiri": 3}, "description": "Ramah, pandai bernegosiasi, diplomatis, dan penuh perhitungan."},
	"Yukong": {"gender": "perempuan", "traits": {"disiplin": 5, "tenang": 4, "empati": 4, "berani": 3}, "description": "Tegas, berdedikasi, berpengalaman, dan sangat menyayangi keluarganya."},
	"Lynx": {"gender": "perempuan", "traits": {"mandiri": 5, "tenang": 4, "berani": 3, "logis": 3}, "description": "Praktis, suka menjelajah, tenang, dan nyaman hidup mandiri."},
	"Topaz": {"gender": "perempuan", "traits": {"ambisius": 5, "logis": 5, "disiplin": 4, "empati": 3}, "description": "Profesional, kompetitif, pintar membaca situasi, dan bertanggung jawab."},
	"Ruan Mei": {"gender": "perempuan", "traits": {"logis": 5, "tenang": 5, "mandiri": 4, "ambisius": 3}, "description": "Jenius yang elegan, fokus pada riset, dan cenderung menjaga jarak emosional."},
	"Black Swan": {"gender": "perempuan", "traits": {"tenang": 5, "logis": 4, "mandiri": 4, "empati": 3}, "description": "Misterius, sabar, observatif, dan gemar memahami kenangan orang lain."},
	"Acheron": {"gender": "perempuan", "traits": {"tenang": 5, "mandiri": 5, "berani": 4, "empati": 3}, "description": "Pendiam, kuat, reflektif, dan menyimpan kesedihan yang sangat dalam."},
	"Sparkle": {"gender": "perempuan", "traits": {"humoris": 5, "spontan": 5, "sosial": 4, "mandiri": 3}, "description": "Usil, teatrikal, sulit diprediksi, dan menikmati kekacauan."},
	"Robin": {"gender": "perempuan", "traits": {"empati": 5, "sosial": 5, "tenang": 4, "berani": 3}, "description": "Hangat, penuh harapan, peduli pada banyak orang, dan berani melindungi keyakinannya."},
	"Firefly": {"gender": "perempuan", "traits": {"berani": 5, "empati": 5, "mandiri": 4, "disiplin": 3}, "description": "Lembut dan tulus, tetapi sangat berani melawan takdirnya."},
	"Jade": {"gender": "perempuan", "traits": {"logis": 5, "ambisius": 5, "tenang": 4, "mandiri": 4}, "description": "Elegan, kalkulatif, persuasif, dan selalu melihat nilai sebuah peluang."},
	"Feixiao": {"gender": "perempuan", "traits": {"berani": 5, "spontan": 4, "ambisius": 4, "sosial": 3}, "description": "Energik, percaya diri, kompetitif, dan sangat menghormati kekuatan."},
	"Tribbie": {"gender": "perempuan", "traits": {"empati": 5, "sosial": 4, "tenang": 3, "berani": 3}, "description": "Penuh kasih, ceria, suportif, dan mampu menyatukan banyak orang."},
	"Aglaea": {"gender": "perempuan", "traits": {"tenang": 5, "disiplin": 4, "empati": 4, "ambisius": 3}, "description": "Anggun, bertanggung jawab, pekerja keras, dan sangat setia pada tugasnya."},
	"Hyacine": {"gender": "perempuan", "traits": {"empati": 5, "sosial": 4, "humoris": 3, "berani": 3}, "description": "Perawat yang hangat, optimistis, lembut, dan berani menghadapi bahaya."},
	"The Herta": {"gender": "perempuan", "traits": {"logis": 5, "mandiri": 5, "ambisius": 4, "humoris": 3}, "description": "Jenius, terus terang, arogan, dan sangat berorientasi pada rasa ingin tahu."},
	"Evanescia": {"gender": "perempuan", "traits": {"tenang": 5, "mandiri": 4, "logis": 4, "empati": 3}, "description": "Karakter misterius dari perkembangan cerita terbaru."},
	"Pearl": {"gender": "perempuan", "traits": {"logis": 5, "disiplin": 5, "tenang": 4, "ambisius": 3}, "description": "Rasional, sangat terorganisasi, dan mengambil keputusan berdasarkan perhitungan."},
	"Dan Heng": {"gender": "laki-laki", "traits": {"tenang": 5, "logis": 4, "mandiri": 4, "disiplin": 4}, "description": "Pendiam, rasional, dapat diandalkan, dan menyimpan masa lalu yang berat."},
	"Welt": {"gender": "laki-laki", "traits": {"tenang": 5, "logis": 5, "empati": 4, "disiplin": 3}, "description": "Dewasa, bijaksana, sabar, dan selalu memikirkan keselamatan orang lain."},
	"Gepard": {"gender": "laki-laki", "traits": {"disiplin": 5, "empati": 4, "berani": 4, "tenang": 3}, "description": "Sopan, jujur, sangat loyal, dan memegang teguh kewajibannya."},
	"Sampo": {"gender": "laki-laki", "traits": {"humoris": 5, "spontan": 4, "sosial": 4, "mandiri": 3}, "description": "Licik, ramah, oportunis, dan selalu punya cara unik untuk bertahan."},
	"Jing Yuan": {"gender": "laki-laki", "traits": {"tenang": 5, "logis": 4, "humoris": 3, "empati": 4}, "description": "Santai namun tajam, bijaksana, strategis, dan sangat peduli pada bawahannya."},
	"Luocha": {"gender": "laki-laki", "traits": {"tenang": 5, "logis": 4, "empati": 3, "mandiri": 4}, "description": "Sopan, misterius, tenang, dan selalu menyembunyikan tujuan sebenarnya."},
	"Blade": {"gender": "laki-laki", "traits": {"mandiri": 5, "berani": 5, "tenang": 3, "empati": 2}, "description": "Pendiam, keras, tidak takut mati, dan digerakkan oleh dendam."},
	"Luka": {"gender": "laki-laki", "traits": {"berani": 5, "sosial": 4, "humoris": 3, "empati": 4}, "description": "Optimistis, ramah, pekerja keras, dan suka membantu komunitasnya."},
	"Argenti": {"gender": "laki-laki", "traits": {"empati": 5, "berani": 4, "sosial": 4, "disiplin": 3}, "description": "Ksatria idealis, sopan, dramatis, dan selalu memuji keindahan."},
	"Dr. Ratio": {"gender": "laki-laki", "traits": {"logis": 5, "ambisius": 4, "mandiri": 4, "humoris": 3}, "description": "Sangat rasional, blak-blakan, percaya diri, dan menuntut orang berpikir."},
	"Aventurine": {"gender": "laki-laki", "traits": {"ambisius": 5, "sosial": 4, "spontan": 4, "logis": 3}, "description": "Karismatik, berani mengambil risiko, manipulatif, dan pandai membaca peluang."},
	"Misha": {"gender": "laki-laki", "traits": {"empati": 5, "tenang": 4, "disiplin": 3, "mandiri": 3}, "description": "Sopan, rajin, pemalu, dan memiliki hati yang sangat tulus."},
	"Gallagher": {"gender": "laki-laki", "traits": {"tenang": 4, "humoris": 4, "empati": 4, "mandiri": 3}, "description": "Santai, misterius, observatif, dan lebih peduli daripada yang ia tunjukkan."},
	"Boothill": {"gender": "laki-laki", "traits": {"berani": 5, "spontan": 5, "humoris": 4, "mandiri": 4}, "description": "Vulgar, berani, penuh gaya, keras kepala, dan sangat setia pada prinsipnya."},
	"Sunday": {"gender": "laki-laki", "traits": {"tenang": 4, "logis": 4, "ambisius": 5, "empati": 3}, "description": "Karismatik, idealis, terstruktur, dan yakin dirinya tahu jalan terbaik."},
	"Moze": {"gender": "laki-laki", "traits": {"mandiri": 5, "tenang": 5, "disiplin": 4, "empati": 2}, "description": "Pendiam, profesional, teliti, dan lebih nyaman bekerja dari balik bayangan."},
	"Mydei": {"gender": "laki-laki", "traits": {"berani": 5, "ambisius": 4, "empati": 4, "spontan": 3}, "description": "Berjiwa pejuang, keras kepala, penuh semangat, dan melindungi orang-orangnya."},
	"Anaxa": {"gender": "laki-laki", "traits": {"logis": 5, "mandiri": 4, "tenang": 3, "ambisius": 4}, "description": "Cerdas, skeptis, tajam dalam berdebat, dan tidak mudah menerima dogma."},
	"Phainon": {"gender": "laki-laki", "traits": {"berani": 5, "empati": 5, "ambisius": 4, "disiplin": 3}, "description": "Pahlawan yang penuh tekad, hangat, rela berkorban, dan memikul tanggung jawab besar."},
	"Cipher": {"gender": "perempuan", "traits": {"spontan": 5, "humoris": 4, "mandiri": 4, "sosial": 3}, "description": "Lincah, oportunis, suka bermain, dan sangat mengandalkan kecerdikan."},
	"Ashveil": {"gender": "laki-laki", "traits": {"tenang": 4, "berani": 4, "mandiri": 4, "disiplin": 3}, "description": "Karakter misterius yang dikenal melalui perkembangan cerita terbaru."},	
	"Mortenax Blade": {"gender": "laki-laki", "traits": {"berani": 5, "mandiri": 5, "tenang": 3, "empati": 2}, "description": "Versi perkembangan terbaru Blade yang tetap keras dan penuh tekad."},
	"Robin Summeretto": {"gender": "perempuan", "traits": {"empati": 5, "sosial": 5, "spontan": 3, "berani": 3}, "description": "Versi musim panas Robin yang ceria, hangat, dan tetap peduli pada orang lain."},
	"Aventurine Waveflair": {"gender": "laki-laki", "traits": {"spontan": 5, "sosial": 4, "ambisius": 4, "humoris": 3}, "description": "Versi musim panas Aventurine yang santai, kompetitif, dan penuh risiko."},
	"Natasha": {"gender": "perempuan", "traits": {"empati": 5, "disiplin": 4, "tenang": 4, "berani": 3}, "description": "Dokter yang lembut, bertanggung jawab, tegas, dan selalu membantu warga."},
	"Serval": {"gender": "perempuan", "traits": {"spontan": 5, "humoris": 4, "sosial": 4, "mandiri": 3}, "description": "Musisi yang bebas, kreatif, berani, dan tidak suka dikekang."},
	"Pela": {"gender": "perempuan", "traits": {"logis": 5, "disiplin": 4, "tenang": 4, "mandiri": 3}, "description": "Teliti, cerdas, profesional, dan sangat dapat diandalkan."},
	"Hook": {"gender": "perempuan", "traits": {"berani": 5, "spontan": 5, "humoris": 4, "empati": 3}, "description": "Pemimpin kecil yang berani, aktif, keras kepala, dan menyayangi kelompoknya."},
	"Clara": {"gender": "perempuan", "traits": {"empati": 5, "tenang": 4, "mandiri": 3, "berani": 3}, "description": "Pemalu, baik hati, penuh rasa ingin tahu, dan sangat peduli pada robot serta manusia."},
	"Sushang": {"gender": "perempuan", "traits": {"berani": 5, "sosial": 4, "spontan": 4, "empati": 3}, "description": "Optimistis, polos, rajin, dan ingin menjadi pahlawan yang hebat."},
	"Hanya": {"gender": "perempuan", "traits": {"disiplin": 5, "tenang": 4, "logis": 4, "empati": 3}, "description": "Serius, pekerja keras, teliti, dan terbiasa memikul beban orang lain."},
	"Xueyi": {"gender": "perempuan", "traits": {"disiplin": 5, "mandiri": 4, "tenang": 4, "berani": 3}, "description": "Tegas, fokus pada tugas, tidak mudah goyah, dan mengejar keadilan."},
	"Guinaifen": {"gender": "perempuan", "traits": {"sosial": 5, "humoris": 5, "spontan": 4, "berani": 3}, "description": "Ekspresif, ramah, kreatif, dan selalu mencari cara menghibur orang lain."},
	"Huohuo": {"gender": "perempuan", "traits": {"empati": 5, "tenang": 3, "disiplin": 4, "berani": 2}, "description": "Pemalu dan mudah takut, tetapi sangat baik hati serta bertanggung jawab."},
	"Yunli": {"gender": "perempuan", "traits": {"berani": 5, "spontan": 4, "ambisius": 4, "humoris": 3}, "description": "Berbakat, kompetitif, keras kepala, dan sangat percaya pada kemampuan sendiri."},
	"Rappa": {"gender": "perempuan", "traits": {"humoris": 5, "spontan": 5, "berani": 4, "mandiri": 3}, "description": "Eksentrik, kreatif, penuh energi, dan melihat dunia seperti pertunjukan."},
	"Lingsha": {"gender": "perempuan", "traits": {"tenang": 5, "empati": 4, "logis": 4, "sosial": 3}, "description": "Dewasa, tenang, penuh perhatian, dan ahli membaca keadaan."},
	"Fugue": {"gender": "perempuan", "traits": {"mandiri": 5, "tenang": 4, "berani": 4, "empati": 3}, "description": "Tangguh, penuh rahasia, adaptif, dan mampu bangkit dari kehilangan."},
	"Arlan": {"gender": "laki-laki", "traits": {"disiplin": 5, "empati": 4, "berani": 4, "mandiri": 3}, "description": "Rajin, rendah hati, loyal, dan rela mengambil risiko demi melindungi orang lain."},
	"Yanqing": {"gender": "laki-laki", "traits": {"berani": 5, "ambisius": 4, "spontan": 3, "disiplin": 3}, "description": "Berbakat, percaya diri, kompetitif, dan sangat bersemangat untuk berkembang."},
	"Jiaoqiu": {"gender": "laki-laki", "traits": {"logis": 5, "tenang": 4, "empati": 4, "humoris": 3}, "description": "Cerdas, tenang, penuh perhitungan, dan memakai humor untuk menyamarkan kepedulian."},
	"Caelus/Stelle": {"gender": "laki-laki", "traits": {"berani": 4, "spontan": 4, "humoris": 4, "mandiri": 4}, "description": "Trailblazer yang adaptif, berani, suka bercanda, dan bebas menentukan jalannya sendiri."},
	"Asta": {"gender": "perempuan", "traits": {"ambisius": 5, "sosial": 4, "logis": 4, "disiplin": 3}, "description": "Pemimpin muda yang cerdas, antusias, dermawan, dan suka menjelajah ilmu."},
	"Herta": {"gender": "perempuan", "traits": {"logis": 5, "mandiri": 5, "ambisius": 4, "humoris": 3}, "description": "Jenius yang terus terang, sangat ingin tahu, dan terbiasa mengandalkan kemampuan sendiri."},
	"Saber": {"gender": "perempuan", "traits": {"disiplin": 5, "berani": 5, "empati": 4, "tenang": 3}, "description": "Ksatria yang teguh, bertanggung jawab, berani, dan memegang sumpahnya."},
	"Archer": {"gender": "laki-laki", "traits": {"logis": 5, "mandiri": 5, "tenang": 4, "berani": 4}, "description": "Pejuang berpengalaman yang skeptis, pragmatis, dan mampu bertindak tanpa banyak bantuan."},
	"Bailu": {"gender": "perempuan", "traits": {"empati": 5, "sosial": 4, "spontan": 4, "berani": 3}, "description": "Tabib kecil yang ceria, penuh energi, dan selalu ingin menolong orang lain."},
	"Jingliu": {"gender": "perempuan", "traits": {"tenang": 5, "mandiri": 5, "disiplin": 4, "berani": 4}, "description": "Pendekar yang dingin, fokus, sangat terampil, dan digerakkan oleh tekad kuat."},
	"Dahlia": {"gender": "perempuan", "traits": {"sosial": 5, "humoris": 4, "spontan": 4, "ambisius": 3}, "description": "Sosok karismatik yang ekspresif, adaptif, dan pandai membaca suasana."},
	"Castorice": {"gender": "perempuan", "traits": {"tenang": 5, "empati": 5, "mandiri": 4, "berani": 3}, "description": "Pribadi pendiam dan reflektif yang menyimpan keteguhan serta kepedulian mendalam."},
	"Hysilens": {"gender": "perempuan", "traits": {"berani": 5, "disiplin": 4, "empati": 4, "tenang": 3}, "description": "Pejuang tangguh yang tegas, setia, dan berani menghadapi ancaman besar."},
	"Cerydra": {"gender": "perempuan", "traits": {"ambisius": 5, "logis": 4, "sosial": 4, "disiplin": 3}, "description": "Tokoh strategis yang percaya diri, persuasif, dan berorientasi pada perubahan."},
	"Evernight": {"gender": "perempuan", "traits": {"tenang": 5, "mandiri": 4, "logis": 4, "empati": 3}, "description": "Sosok misterius yang sabar, observatif, dan mampu menyimpan banyak rahasia."},
	"Dan Heng Permansor Terrae": {"gender": "laki-laki", "traits": {"tenang": 5, "disiplin": 5, "empati": 4, "berani": 3}, "description": "Pelindung yang tenang, dapat diandalkan, dan bersedia memikul tanggung jawab besar."},
	"Cyrene": {"gender": "perempuan", "traits": {"empati": 5, "sosial": 4, "tenang": 4, "humoris": 3}, "description": "Pribadi hangat yang penuh perhatian, mudah membangun koneksi, dan membawa harapan."},
	"Sparxie": {"gender": "perempuan", "traits": {"spontan": 5, "humoris": 5, "sosial": 4, "mandiri": 3}, "description": "Karakter energik yang usil, kreatif, sulit diprediksi, dan menyukai kebebasan."},
	"Yao Guang": {"gender": "perempuan", "traits": {"logis": 5, "tenang": 4, "ambisius": 4, "disiplin": 3}, "description": "Sosok analitis yang teliti, strategis, dan terbiasa melihat gambaran besar."},
	"Silver Wolf Lv999": {"gender": "perempuan", "traits": {"logis": 5, "humoris": 4, "mandiri": 4, "spontan": 3}, "description": "Versi ekstrem Silver Wolf yang tetap jenius, santai, kompetitif, dan menganggap dunia sebagai permainan."},
	"Rin Tohsaka": {"gender": "perempuan", "traits": {"ambisius": 5, "logis": 4, "disiplin": 4, "berani": 3}, "description": "Penyihir yang cerdas, percaya diri, kompetitif, dan tetap peduli pada orang terdekatnya."},
	"Gilgamesh": {"gender": "laki-laki", "traits": {"ambisius": 5, "berani": 5, "mandiri": 4, "humoris": 3}, "description": "Raja yang sangat percaya diri, dominan, berkemauan kuat, dan tidak mudah tunduk pada siapa pun."},
	"Himeko Nova": {"gender": "perempuan", "traits": {"tenang": 5, "ambisius": 4, "empati": 4, "berani": 3}, "description": "Versi alternatif Himeko yang dewasa, tegas, bertanggung jawab, dan rela berkorban demi tujuan besar."},
	
}


TRAIT_DETAILS = {
	"tenang": {
		"label": "stabilitas emosional",
		"overview": "Kemampuan menjaga kejernihan pikiran dan mengatur respons ketika keadaan berubah atau terasa berat.",
		"strength": "mampu menjaga kepala tetap dingin dan tidak mudah terbawa suasana",
		"signals": "Biasanya mengambil jeda, menyusun prioritas, lalu merespons dengan terukur.",
		"risk": "bisa terlihat terlalu tertutup atau menunda mengungkapkan perasaan",
		"balance": "Tetap beri ruang untuk merasakan dan membicarakan emosi, bukan hanya mengendalikannya.",
	},
	"berani": {
		"label": "keberanian bertindak",
		"overview": "Dorongan untuk mengambil sikap, mencoba, dan melindungi hal yang dianggap penting meskipun ada risiko.",
		"strength": "berani mengambil sikap ketika orang lain masih ragu",
		"signals": "Cenderung maju lebih dulu, menyampaikan pendapat, dan tidak mudah mundur saat situasi sulit.",
		"risk": "bisa terlalu cepat mengambil risiko sebelum semua akibat dipertimbangkan",
		"balance": "Bedakan keberanian dari terburu-buru dengan memeriksa dampak sebelum bergerak.",
	},
	"logis": {
		"label": "cara berpikir analitis",
		"overview": "Kecenderungan memahami dunia melalui fakta, pola, sebab-akibat, dan pertimbangan yang bisa diuji.",
		"strength": "memecah masalah menjadi fakta, pola, dan langkah yang bisa dikerjakan",
		"signals": "Sering bertanya mengapa, membandingkan pilihan, dan mencari bukti sebelum percaya.",
		"risk": "bisa terlalu kritis dan sulit memberi ruang bagi keputusan emosional",
		"balance": "Gunakan data sebagai kompas, tetapi jangan mengabaikan konteks manusia di balik masalah.",
	},
	"empati": {
		"label": "kepekaan interpersonal",
		"overview": "Kemampuan menangkap kebutuhan, perasaan, dan batas orang lain lalu merespons dengan kepedulian.",
		"strength": "peka terhadap kebutuhan, perasaan, dan batasan orang lain",
		"signals": "Mendengarkan dengan sungguh-sungguh, membaca suasana, dan menawarkan bantuan yang relevan.",
		"risk": "bisa terlalu sering mendahulukan kebutuhan orang lain daripada diri sendiri",
		"balance": "Kepedulian akan lebih sehat ketika batas pribadi dan kebutuhanmu ikut diperhitungkan.",
	},
	"mandiri": {
		"label": "kemandirian",
		"overview": "Kapasitas menentukan arah, mengambil tanggung jawab, dan tetap bergerak tanpa menunggu validasi terus-menerus.",
		"strength": "mampu menentukan arah dan menyelesaikan masalah tanpa banyak bergantung",
		"signals": "Nyaman bekerja sendiri, menjaga ruang pribadi, dan mengambil keputusan berdasarkan nilai sendiri.",
		"risk": "bisa sulit meminta bantuan atau membiarkan orang lain ikut berperan",
		"balance": "Meminta bantuan pada waktu yang tepat bukan kehilangan kendali, melainkan membangun dukungan.",
	},
	"spontan": {
		"label": "fleksibilitas dan spontanitas",
		"overview": "Kesiapan beradaptasi, mengikuti peluang, dan menemukan pendekatan baru ketika rencana awal tidak berjalan.",
		"strength": "cepat beradaptasi dan mampu menemukan peluang dari perubahan mendadak",
		"signals": "Menyukai variasi, cepat mencoba hal baru, dan tidak mudah lumpuh ketika keadaan berubah.",
		"risk": "bisa mudah bosan pada rutinitas atau kurang sabar dengan rencana panjang",
		"balance": "Sisakan struktur minimum agar kebebasan bergerak tetap menghasilkan kemajuan yang konsisten.",
	},
	"disiplin": {
		"label": "konsistensi dan tanggung jawab",
		"overview": "Kemampuan menjaga komitmen, mengatur langkah, dan menyelesaikan sesuatu bahkan ketika motivasi sedang turun.",
		"strength": "dapat dipercaya untuk menjaga komitmen sampai tugas benar-benar selesai",
		"signals": "Membuat sistem, menghormati tenggat, dan tetap hadir ketika orang lain membutuhkan kepastian.",
		"risk": "bisa terlalu keras pada diri sendiri dan kurang lentur terhadap perubahan",
		"balance": "Rencana yang baik perlu memiliki jeda dan ruang revisi agar tidak berubah menjadi tekanan.",
	},
	"sosial": {
		"label": "energi sosial",
		"overview": "Kecenderungan membangun koneksi, bertukar energi melalui interaksi, dan membuat kelompok terasa hidup.",
		"strength": "mudah membangun koneksi dan membuat orang lain merasa dilibatkan",
		"signals": "Cepat membuka percakapan, menikmati kolaborasi, dan peka pada dinamika kelompok.",
		"risk": "bisa terlalu dipengaruhi suasana kelompok atau sulit menikmati kesendirian",
		"balance": "Jaga waktu sunyi agar keputusanmu tetap berasal dari kebutuhanmu, bukan hanya respons lingkungan.",
	},
	"ambisius": {
		"label": "dorongan berprestasi",
		"overview": "Energi untuk menetapkan target, meningkatkan kemampuan, dan mengubah potensi menjadi pencapaian nyata.",
		"strength": "memiliki target jelas dan kemauan untuk terus berkembang",
		"signals": "Menetapkan standar tinggi, mencari tantangan, dan melihat kegagalan sebagai bahan evaluasi.",
		"risk": "bisa terlalu fokus pada hasil sampai lupa memulihkan diri",
		"balance": "Ukur keberhasilan juga dari proses, kesehatan, dan hubungan yang tetap terjaga.",
	},
	"humoris": {
		"label": "keluwesan humor",
		"overview": "Kemampuan menemukan sudut pandang ringan, mencairkan ketegangan, dan menjaga kelenturan emosi dalam situasi sulit.",
		"strength": "mampu meredakan ketegangan dan melihat sisi ringan dari situasi sulit",
		"signals": "Menggunakan candaan untuk membangun kedekatan, memulihkan suasana, dan membantu orang bernapas sejenak.",
		"risk": "bisa memakai candaan untuk menghindari pembicaraan yang rentan atau serius",
		"balance": "Pastikan humor menjadi jembatan menuju kejujuran, bukan cara untuk terus menghindarinya.",
	},
}


QUESTIONS = [
	(
		"Saat menghadapi masalah besar, apa yang paling sering kamu lakukan?",
		[
			Answer("Menenangkan diri lalu menyusun rencana.", {"tenang": 3, "logis": 2}),
			Answer("Langsung bertindak sebelum masalah membesar.", {"berani": 3, "spontan": 2}),
			Answer("Mencari pendapat dari orang yang dipercaya.", {"sosial": 2, "empati": 2}),
			Answer("Menghindarinya sebentar sampai siap.", {"mandiri": 1, "tenang": 1}),
		],
	),
	(
		"Di dalam kelompok, peran yang paling cocok untukmu adalah...",
		[
			Answer("Pemimpin yang menentukan arah.", {"berani": 2, "ambisius": 2}),
			Answer("Pengamat yang memberi analisis.", {"logis": 3, "tenang": 1}),
			Answer("Orang yang menjaga semua tetap kompak.", {"empati": 3, "sosial": 2}),
			Answer("Orang yang mengerjakan tugas sendiri.", {"mandiri": 3, "disiplin": 1}),
		],
	),
	(
		"Kalau rencana tiba-tiba berubah, reaksimu biasanya...",
		[
			Answer("Menyesuaikan diri dan mencari celah baru.", {"spontan": 3, "berani": 1}),
			Answer("Kesal karena ingin semuanya teratur.", {"disiplin": 3, "tenang": -1}),
			Answer("Menganalisis perubahan sebelum memilih langkah.", {"logis": 3}),
			Answer("Mengikuti keputusan mayoritas.", {"sosial": 2, "empati": 1}),
		],
	),
	(
		"Apa yang paling kamu hargai dari seorang teman?",
		[
			Answer("Kejujuran.", {"logis": 1, "mandiri": 1}),
			Answer("Kesetiaan.", {"empati": 3, "disiplin": 1}),
			Answer("Keberanian untuk membela yang benar.", {"berani": 3}),
			Answer("Kemampuan membuat suasana menyenangkan.", {"humoris": 3, "sosial": 1}),
		],
	),
	(
		"Ketika melihat orang lain sedang kesulitan, kamu...",
		[
			Answer("Langsung menawarkan bantuan.", {"empati": 3, "berani": 1}),
			Answer("Mencari tahu bantuan paling efektif.", {"logis": 3, "empati": 1}),
			Answer("Memberi ruang, lalu membantu jika diminta.", {"mandiri": 2, "tenang": 1}),
			Answer("Mencairkan suasana dengan humor.", {"humoris": 3, "sosial": 1}),
		],
	),
	(
		"Bagaimana gaya belajarmu?",
		[
			Answer("Terjadwal dan konsisten.", {"disiplin": 3}),
			Answer("Memahami konsep dan alasannya.", {"logis": 3}),
			Answer("Belajar lewat praktik langsung.", {"berani": 2, "spontan": 2}),
			Answer("Berdiskusi bersama orang lain.", {"sosial": 3}),
		],
	),
	(
		"Saat mengambil keputusan penting, kamu lebih mengandalkan...",
		[
			Answer("Data dan fakta.", {"logis": 3}),
			Answer("Perasaan dan intuisi.", {"empati": 2, "spontan": 1}),
			Answer("Pengalaman masa lalu.", {"tenang": 2, "disiplin": 1}),
			Answer("Dorongan untuk mencoba sesuatu baru.", {"berani": 2, "ambisius": 2}),
		],
	),
	(
		"Apa yang biasanya kamu lakukan saat sedang stres?",
		[
			Answer("Menyendiri dan menata pikiran.", {"mandiri": 2, "tenang": 2}),
			Answer("Bercerita kepada seseorang.", {"sosial": 2, "empati": 2}),
			Answer("Menyibukkan diri dengan pekerjaan.", {"disiplin": 2, "ambisius": 1}),
			Answer("Melakukan hal spontan yang menyenangkan.", {"spontan": 3, "humoris": 1}),
		],
	),
	(
		"Target hidup yang paling menarik bagimu adalah...",
		[
			Answer("Menjadi versi terbaik dari diri sendiri.", {"ambisius": 3, "mandiri": 1}),
			Answer("Menciptakan kehidupan yang stabil.", {"tenang": 3, "disiplin": 1}),
			Answer("Membantu banyak orang.", {"empati": 3}),
			Answer("Mendapat pengalaman sebanyak mungkin.", {"spontan": 3, "berani": 1}),
		],
	),
	(
		"Seberapa mudah kamu memaafkan orang lain?",
		[
			Answer("Mudah, semua orang bisa salah.", {"empati": 3}),
			Answer("Tergantung seberapa serius kesalahannya.", {"logis": 2, "tenang": 1}),
			Answer("Sulit, kepercayaan harus dibangun lagi.", {"mandiri": 2, "disiplin": 1}),
			Answer("Saya membuat lelucon lalu move on.", {"humoris": 3, "spontan": 1}),
		],
	),
	(
		"Di waktu luang, kamu lebih suka...",
		[
			Answer("Membaca atau mempelajari sesuatu.", {"logis": 2, "tenang": 1}),
			Answer("Bertemu teman dan mengobrol.", {"sosial": 3}),
			Answer("Mencoba kegiatan baru.", {"spontan": 3, "berani": 1}),
			Answer("Menyelesaikan proyek pribadi.", {"mandiri": 2, "disiplin": 2}),
		],
	),
	(
		"Apa yang paling membuatmu marah?",
		[
			Answer("Ketidakadilan.", {"berani": 2, "empati": 2}),
			Answer("Orang yang tidak bertanggung jawab.", {"disiplin": 3}),
			Answer("Kebohongan dan manipulasi.", {"logis": 2, "mandiri": 1}),
			Answer("Suasana yang terlalu serius.", {"humoris": 3}),
		],
	),
	(
		"Saat berdebat, kamu cenderung...",
		[
			Answer("Mencari argumen yang paling masuk akal.", {"logis": 3}),
			Answer("Menyampaikan perasaan dengan jujur.", {"empati": 2, "berani": 1}),
			Answer("Mengalah agar hubungan tetap baik.", {"tenang": 2, "empati": 2}),
			Answer("Membuat suasana lebih ringan.", {"humoris": 2, "sosial": 1}),
		],
	),
	(
		"Kamu paling nyaman jika...",
		[
			Answer("Memiliki kendali atas pilihan sendiri.", {"mandiri": 3}),
			Answer("Semua orang saling mendukung.", {"sosial": 2, "empati": 2}),
			Answer("Ada tantangan yang harus ditaklukkan.", {"ambisius": 3, "berani": 1}),
			Answer("Lingkungan berjalan damai dan teratur.", {"tenang": 2, "disiplin": 2}),
		],
	),
	(
		"Bagaimana kamu menunjukkan rasa sayang?",
		[
			Answer("Mendengarkan dan memahami.", {"empati": 3}),
			Answer("Membantu menyelesaikan masalah.", {"logis": 2, "disiplin": 1}),
			Answer("Mengajak melakukan hal seru.", {"spontan": 2, "humoris": 2}),
			Answer("Selalu hadir dan bisa diandalkan.", {"disiplin": 2, "tenang": 1}),
		],
	),
	(
		"Kalau gagal mencapai sesuatu, kamu...",
		[
			Answer("Menganalisis kesalahan dan mencoba lagi.", {"logis": 2, "ambisius": 2}),
			Answer("Mengambil waktu untuk memulihkan diri.", {"tenang": 3}),
			Answer("Mencari cara yang benar-benar berbeda.", {"spontan": 2, "berani": 2}),
			Answer("Meminta dukungan orang terdekat.", {"sosial": 2, "empati": 1}),
		],
	),
	(
		"Orang biasanya mengenalmu sebagai pribadi yang...",
		[
			Answer("Rasional dan dapat dipercaya.", {"logis": 2, "disiplin": 1}),
			Answer("Hangat dan perhatian.", {"empati": 3}),
			Answer("Berani dan penuh energi.", {"berani": 3, "spontan": 1}),
			Answer("Tenang dan sulit ditebak.", {"tenang": 3, "mandiri": 1}),
		],
	),
	(
		"Jika mendapat kesempatan besar dengan risiko tinggi, kamu...",
		[
			Answer("Mengambilnya setelah menghitung risiko.", {"logis": 2, "berani": 1}),
			Answer("Langsung mengambil kesempatan itu.", {"berani": 3, "spontan": 1}),
			Answer("Menolaknya demi kestabilan.", {"tenang": 2, "disiplin": 1}),
			Answer("Bertanya pada orang yang terdampak.", {"empati": 2, "sosial": 1}),
		],
	),
	(
		"Menurutmu, kekuatan terbesar seseorang berasal dari...",
		[
			Answer("Pengetahuan dan cara berpikir.", {"logis": 3}),
			Answer("Hati yang peduli pada sesama.", {"empati": 3}),
			Answer("Kemauan untuk terus maju.", {"ambisius": 3, "disiplin": 1}),
			Answer("Kebebasan menjadi diri sendiri.", {"mandiri": 3}),
		],
	),
	(
		"Kalimat mana yang paling menggambarkanmu?",
		[
			Answer("Saya akan menemukan jalan yang paling tepat.", {"logis": 2, "tenang": 1}),
			Answer("Saya tidak akan meninggalkan orang yang penting bagi saya.", {"empati": 2, "disiplin": 1}),
			Answer("Saya ingin melihat apa yang ada di balik cakrawala.", {"spontan": 2, "berani": 2}),
			Answer("Saya menentukan arah hidup saya sendiri.", {"mandiri": 2, "ambisius": 2}),
		],
	),
	(
		"Saat pertama bertemu orang baru, kamu biasanya...",
		[
			Answer("Mengamati dulu sebelum bicara.", {"tenang": 2, "logis": 1}),
			Answer("Langsung menyapa dan mengobrol.", {"sosial": 3}),
			Answer("Membuat candaan untuk mencairkan suasana.", {"humoris": 3}),
			Answer("Menunggu mereka memulai percakapan.", {"mandiri": 1, "tenang": 1}),
		],
	),
	(
		"Bagaimana sikapmu terhadap aturan?",
		[
			Answer("Aturan penting agar semuanya tertib.", {"disiplin": 3}),
			Answer("Aturan boleh dilanggar jika tidak masuk akal.", {"mandiri": 2, "logis": 2}),
			Answer("Saya mengikuti aturan selama tidak merugikan siapa pun.", {"empati": 2, "tenang": 1}),
			Answer("Saya lebih suka mencari celah di dalamnya.", {"spontan": 2, "humoris": 1}),
		],
	),
	(
		"Jika temanmu mengambil keputusan buruk, kamu akan...",
		[
			Answer("Menjelaskan akibatnya dengan tenang.", {"logis": 3, "empati": 1}),
			Answer("Tetap mendukungnya sambil membantu memperbaiki keadaan.", {"empati": 3}),
			Answer("Membiarkannya belajar dari pengalaman.", {"mandiri": 2, "tenang": 1}),
			Answer("Mengajaknya melakukan sesuatu agar tidak terlalu stres.", {"humoris": 2, "sosial": 1}),
		],
	),
	(
		"Apa yang paling membuatmu merasa puas?",
		[
			Answer("Memecahkan masalah yang sulit.", {"logis": 3}),
			Answer("Melihat orang yang saya sayangi bahagia.", {"empati": 3}),
			Answer("Mencapai sesuatu yang dianggap mustahil.", {"ambisius": 3, "berani": 1}),
			Answer("Menjalani hari tanpa banyak tekanan.", {"tenang": 3}),
		],
	),
	(
		"Ketika rencana kelompok gagal, kamu cenderung...",
		[
			Answer("Mencari penyebabnya agar tidak terulang.", {"logis": 3}),
			Answer("Menyemangati semua orang untuk mencoba lagi.", {"empati": 2, "sosial": 2}),
			Answer("Mengambil alih dan membuat rencana baru.", {"berani": 2, "ambisius": 2}),
			Answer("Mencari pendekatan yang lebih kreatif.", {"spontan": 3, "humoris": 1}),
		],
	),
	(
		"Seberapa penting pengakuan orang lain bagimu?",
		[
			Answer("Penting, itu menunjukkan hasil kerja saya dihargai.", {"ambisius": 3, "sosial": 1}),
			Answer("Tidak terlalu penting, saya tahu kemampuan saya.", {"mandiri": 3}),
			Answer("Penting jika datang dari orang yang saya hormati.", {"empati": 2, "disiplin": 1}),
			Answer("Saya lebih suka mengejutkan mereka dengan hasil.", {"spontan": 2, "humoris": 1}),
		],
	),
	(
		"Dalam persahabatan, kamu lebih sering menjadi orang yang...",
		[
			Answer("Memberi nasihat yang masuk akal.", {"logis": 2, "tenang": 1}),
			Answer("Mendengarkan semua keluh kesah.", {"empati": 3}),
			Answer("Mengajak semua orang melakukan hal baru.", {"spontan": 2, "sosial": 2}),
			Answer("Menjaga rahasia dan selalu hadir.", {"disiplin": 2, "mandiri": 1}),
		],
	),
	(
		"Kalau harus memilih, kamu lebih takut pada...",
		[
			Answer("Kehilangan kendali atas keadaan.", {"logis": 2, "disiplin": 2}),
			Answer("Mengecewakan orang yang penting.", {"empati": 3}),
			Answer("Hidup tanpa tantangan.", {"ambisius": 3, "spontan": 1}),
			Answer("Kehilangan kebebasan.", {"mandiri": 3}),
		],
	),
	(
		"Bagaimana kamu menghadapi kritik?",
		[
			Answer("Menganalisis apakah kritik itu benar.", {"logis": 3}),
			Answer("Mencoba memahami maksud orang tersebut.", {"empati": 2, "tenang": 1}),
			Answer("Menjadikannya motivasi untuk membuktikan diri.", {"ambisius": 3}),
			Answer("Membalasnya dengan candaan.", {"humoris": 3}),
		],
	),
	(
		"Tempat ideal untuk mengisi energi adalah...",
		[
			Answer("Ruangan tenang dengan buku atau musik.", {"tenang": 3}),
			Answer("Tempat ramai bersama orang-orang dekat.", {"sosial": 3}),
			Answer("Tempat baru yang belum pernah dikunjungi.", {"spontan": 3}),
			Answer("Tempat yang bisa saya atur sendiri.", {"mandiri": 3}),
		],
	),
	(
		"Jika mendapat rahasia besar, kamu akan...",
		[
			Answer("Menjaganya dengan sangat hati-hati.", {"disiplin": 3, "tenang": 1}),
			Answer("Mencari tahu kebenaran di baliknya.", {"logis": 3}),
			Answer("Menceritakannya hanya kepada orang terpercaya.", {"sosial": 2, "empati": 2}),
			Answer("Memanfaatkannya jika situasi memaksa.", {"mandiri": 2, "ambisius": 2}),
		],
	),
	(
		"Saat marah, kamu paling mungkin...",
		[
			Answer("Diam sampai pikiran kembali jernih.", {"tenang": 3}),
			Answer("Mengatakan semuanya secara langsung.", {"berani": 3}),
			Answer("Menjelaskan mengapa tindakan itu salah.", {"logis": 2, "disiplin": 1}),
			Answer("Membuat lelucon sinis.", {"humoris": 3, "mandiri": 1}),
		],
	),
	(
		"Apa arti kebebasan bagimu?",
		[
			Answer("Bisa memilih jalan hidup sendiri.", {"mandiri": 3}),
			Answer("Tidak dikekang oleh aturan yang tidak adil.", {"berani": 2, "logis": 1}),
			Answer("Bisa hidup tanpa menyakiti orang lain.", {"empati": 3}),
			Answer("Bisa mencoba apa pun yang menarik.", {"spontan": 3}),
		],
	),
	(
		"Bagaimana gaya kepemimpinanmu?",
		[
			Answer("Membuat rencana jelas dan membagi tugas.", {"disiplin": 3, "logis": 1}),
			Answer("Memimpin dari depan dan mengambil risiko.", {"berani": 3}),
			Answer("Mendengarkan semua anggota lebih dulu.", {"empati": 2, "sosial": 2}),
			Answer("Memberi ruang agar semua orang berinisiatif.", {"mandiri": 2, "tenang": 1}),
		],
	),
	(
		"Apa yang biasanya kamu lakukan ketika bosan?",
		[
			Answer("Mempelajari topik baru.", {"logis": 3}),
			Answer("Menghubungi teman.", {"sosial": 3}),
			Answer("Mencoba hobi atau tempat baru.", {"spontan": 3}),
			Answer("Bermimpi dan membuat rencana pribadi.", {"mandiri": 2, "ambisius": 1}),
		],
	),
	(
		"Apa yang paling kamu cari dari pasangan atau teman dekat?",
		[
			Answer("Percakapan yang cerdas.", {"logis": 3}),
			Answer("Rasa aman dan pengertian.", {"empati": 3, "tenang": 1}),
			Answer("Petualangan dan kejutan.", {"spontan": 3, "berani": 1}),
			Answer("Seseorang yang menghormati ruang pribadi.", {"mandiri": 3}),
		],
	),
	(
		"Saat melihat ketidakadilan, kamu akan...",
		[
			Answer("Mengumpulkan fakta sebelum bertindak.", {"logis": 3}),
			Answer("Langsung membela pihak yang dirugikan.", {"berani": 3, "empati": 1}),
			Answer("Mencari jalan damai bagi semua pihak.", {"tenang": 2, "empati": 2}),
			Answer("Membongkar sistemnya dari dalam.", {"mandiri": 2, "ambisius": 2}),
		],
	),
	(
		"Bagaimana kamu menyusun tujuan?",
		[
			Answer("Membuat langkah dan tenggat yang jelas.", {"disiplin": 3}),
			Answer("Menentukan tujuan besar lalu bergerak.", {"ambisius": 3, "berani": 1}),
			Answer("Mengikuti kesempatan yang muncul.", {"spontan": 3}),
			Answer("Menyesuaikannya dengan kebutuhan orang lain.", {"empati": 3}),
		],
	),
	(
		"Kalau hidupmu menjadi sebuah cerita, genrenya paling mungkin...",
		[
			Answer("Misteri penuh teka-teki.", {"logis": 2, "tenang": 2}),
			Answer("Petualangan penuh aksi.", {"berani": 3, "spontan": 2}),
			Answer("Drama tentang hubungan manusia.", {"empati": 3, "sosial": 1}),
			Answer("Komedi absurd yang tidak terduga.", {"humoris": 4}),
		],
	),
	(
		"Pernyataan mana yang paling dekat dengan prinsipmu?",
		[
			Answer("Kebenaran harus dicari, bukan sekadar dipercaya.", {"logis": 3}),
			Answer("Tidak ada yang boleh ditinggalkan sendirian.", {"empati": 3}),
			Answer("Takdir bukan alasan untuk berhenti melawan.", {"berani": 2, "ambisius": 2}),
			Answer("Saya memilih jalan saya sendiri.", {"mandiri": 3}),
		],
	),
	(
		"Ketika seseorang yang kamu percaya berbohong, apa yang paling mungkin kamu lakukan?",
		[
			Answer("Meminta penjelasan dan memeriksa fakta sebelum menyimpulkan.", {"logis": 3, "tenang": 1}),
			Answer("Mengatakan bahwa kebohongan itu menyakiti saya.", {"berani": 2, "empati": 2}),
			Answer("Memberi kesempatan kedua, tetapi mengamati tindakannya.", {"empati": 2, "disiplin": 1}),
			Answer("Mengakhiri hubungan tanpa banyak penjelasan.", {"mandiri": 3, "tenang": 1}),
		],
	),
	(
		"Dalam proyek dengan tenggat waktu dekat, kamu lebih mungkin...",
		[
			Answer("Membuat daftar prioritas dan membagi waktu.", {"disiplin": 3, "logis": 1}),
			Answer("Bekerja dengan intensitas tinggi sampai selesai.", {"ambisius": 3, "berani": 1}),
			Answer("Meminta bantuan agar beban terbagi.", {"sosial": 2, "empati": 2}),
			Answer("Mengubah strategi jika cara pertama tidak efektif.", {"spontan": 3, "mandiri": 1}),
		],
	),
	(
		"Jika pendapatmu ditolak oleh seluruh kelompok, kamu akan...",
		[
			Answer("Menerima keputusan sambil memastikan risikonya dipahami.", {"tenang": 2, "sosial": 1}),
			Answer("Menyampaikan argumen terakhir dengan tegas.", {"berani": 3, "logis": 1}),
			Answer("Mencari kompromi yang masih melindungi tujuan utama.", {"empati": 2, "logis": 2}),
			Answer("Mengerjakan versiku sendiri jika hasil kelompok gagal.", {"mandiri": 3}),
		],
	),
	(
		"Apa reaksimu ketika menerima tanggung jawab yang tidak kamu minta?",
		[
			Answer("Menerimanya dan membuat sistem agar bisa ditangani.", {"disiplin": 3, "tenang": 1}),
			Answer("Menolaknya jika pembagiannya tidak adil.", {"berani": 3, "mandiri": 1}),
			Answer("Menerimanya jika itu membantu orang yang membutuhkan.", {"empati": 3}),
			Answer("Mencari cara kreatif agar tugasnya tidak terasa berat.", {"humoris": 2, "spontan": 2}),
		],
	),
	(
		"Saat berada di lingkungan baru yang tidak kamu kenal, kamu biasanya...",
		[
			Answer("Mempelajari aturan dan pola lingkungan lebih dulu.", {"logis": 2, "tenang": 2}),
			Answer("Mencari satu orang untuk diajak berkenalan.", {"sosial": 3, "empati": 1}),
			Answer("Mencoba hal paling menarik tanpa terlalu banyak berpikir.", {"spontan": 3, "berani": 1}),
			Answer("Membuat rutinitas sendiri agar tetap nyaman.", {"mandiri": 2, "disiplin": 2}),
		],
	),
	(
		"Apa yang kamu lakukan ketika emosimu terlalu penuh untuk berpikir jernih?",
		[
			Answer("Menjauh sebentar dan menenangkan diri.", {"tenang": 3, "mandiri": 1}),
			Answer("Mencurahkan semuanya kepada orang yang dipercaya.", {"sosial": 2, "empati": 2}),
			Answer("Menyalurkannya melalui aktivitas fisik atau tindakan nyata.", {"berani": 2, "disiplin": 1}),
			Answer("Menggunakan humor supaya suasana tidak semakin berat.", {"humoris": 3}),
		],
	),
	(
		"Bagaimana kamu memandang kegagalan yang berulang?",
		[
			Answer("Saya perlu menganalisis pola kesalahannya.", {"logis": 3}),
			Answer("Saya akan terus mencoba sampai menemukan cara yang berhasil.", {"ambisius": 3, "disiplin": 1}),
			Answer("Saya mengubah pendekatan secara total.", {"spontan": 3, "berani": 1}),
			Answer("Saya meminta perspektif orang lain agar tidak terjebak sendiri.", {"sosial": 2, "empati": 1}),
		],
	),
	(
		"Jika menemukan peluang yang menguntungkan tetapi merugikan orang lain, kamu...",
		[
			Answer("Menghitung apakah ada alternatif yang lebih adil.", {"logis": 2, "empati": 2}),
			Answer("Menolaknya meskipun kesempatan itu sangat besar.", {"empati": 3, "disiplin": 1}),
			Answer("Mengambilnya jika saya bisa memperbaiki dampaknya nanti.", {"ambisius": 2, "berani": 2}),
			Answer("Mencari cara memanfaatkan aturan tanpa merugikan siapa pun.", {"mandiri": 2, "spontan": 2}),
		],
	),
	(
		"Seberapa mudah kamu mengubah pendirian setelah mendapat bukti baru?",
		[
			Answer("Saya mengubahnya jika bukti itu kuat.", {"logis": 3}),
			Answer("Saya mempertimbangkan dampaknya pada orang-orang yang terlibat.", {"empati": 2, "tenang": 1}),
			Answer("Saya tetap bertahan jika tujuan akhirnya belum tercapai.", {"ambisius": 2, "disiplin": 1}),
			Answer("Saya tidak masalah berubah arah jika ada kemungkinan yang lebih menarik.", {"spontan": 3}),
		],
	),
	(
		"Ketika seseorang meminta bantuan di saat kamu sendiri sedang lelah, kamu...",
		[
			Answer("Menentukan apakah saya masih sanggup membantu secara realistis.", {"logis": 2, "mandiri": 1}),
			Answer("Tetap membantu sebisa mungkin karena saya tidak tega.", {"empati": 3}),
			Answer("Menjelaskan batas saya dan menawarkan waktu lain.", {"tenang": 2, "disiplin": 2}),
			Answer("Mencari solusi cepat agar masalahnya segera selesai.", {"berani": 2, "spontan": 1}),
		],
	),
	(
		"Apa yang paling sering mengganggu fokusmu?",
		[
			Answer("Informasi yang tidak jelas atau tidak konsisten.", {"logis": 3}),
			Answer("Konflik yang belum diselesaikan.", {"empati": 2, "tenang": 1}),
			Answer("Rutinitas yang terlalu berulang.", {"spontan": 3}),
			Answer("Orang yang tidak menepati komitmen.", {"disiplin": 3}),
		],
	),
	(
		"Saat menjadi pusat perhatian, kamu biasanya...",
		[
			Answer("Berbicara seperlunya dan tetap terstruktur.", {"tenang": 2, "disiplin": 1}),
			Answer("Menikmatinya dan mengajak orang lain ikut terlibat.", {"sosial": 3}),
			Answer("Menggunakannya untuk menyampaikan sesuatu yang penting.", {"berani": 2, "ambisius": 1}),
			Answer("Membuat pertunjukan spontan atau candaan.", {"humoris": 3, "spontan": 1}),
		],
	),
	(
		"Jika harus memilih antara keamanan dan pengalaman baru, kamu akan...",
		[
			Answer("Memilih keamanan jika risikonya belum jelas.", {"tenang": 2, "logis": 1}),
			Answer("Memilih pengalaman baru karena kesempatan belum tentu datang lagi.", {"spontan": 3, "berani": 1}),
			Answer("Mencari cara untuk mendapatkan keduanya.", {"logis": 2, "mandiri": 1}),
			Answer("Memilih berdasarkan siapa saja yang bisa ikut bersamaku.", {"sosial": 2, "empati": 1}),
		],
	),
	(
		"Bagaimana kamu menggunakan uang atau sumber daya yang kamu miliki?",
		[
			Answer("Membuat anggaran dan memikirkan kebutuhan jangka panjang.", {"disiplin": 3, "logis": 1}),
			Answer("Menggunakannya untuk mengejar target yang lebih besar.", {"ambisius": 3}),
			Answer("Menggunakannya untuk pengalaman yang berkesan.", {"spontan": 3}),
			Answer("Berbagi dengan orang yang sedang membutuhkan.", {"empati": 3}),
		],
	),
	(
		"Jika kamu menemukan kesalahan kecil yang tidak akan diketahui siapa pun, kamu...",
		[
			Answer("Memperbaikinya karena kualitas tetap penting.", {"disiplin": 3}),
			Answer("Mencatatnya dan memperbaikinya jika mulai berdampak.", {"logis": 2, "tenang": 1}),
			Answer("Mengakuinya agar tidak menjadi masalah bagi orang lain.", {"empati": 3}),
			Answer("Membiarkannya jika ada hal yang lebih penting untuk dikerjakan.", {"mandiri": 2, "spontan": 1}),
		],
	),
	(
		"Apa yang kamu lakukan ketika orang lain salah memahami niatmu?",
		[
			Answer("Menjelaskan maksud saya dengan contoh yang jelas.", {"logis": 3}),
			Answer("Mendengarkan perasaan mereka sebelum menjelaskan diri.", {"empati": 3}),
			Answer("Membiarkannya jika hubungan itu tidak terlalu penting.", {"mandiri": 2, "tenang": 1}),
			Answer("Mencairkan keadaan dengan candaan lalu membicarakannya.", {"humoris": 3, "sosial": 1}),
		],
	),
	(
		"Dalam diskusi panjang, peran yang paling sering kamu ambil adalah...",
		[
			Answer("Menguji argumen dan mencari celah logikanya.", {"logis": 3}),
			Answer("Menjaga agar semua orang mendapat kesempatan bicara.", {"empati": 2, "sosial": 2}),
			Answer("Mendorong diskusi menuju keputusan.", {"berani": 2, "ambisius": 1}),
			Answer("Menyelipkan sudut pandang tidak biasa.", {"spontan": 2, "humoris": 2}),
		],
	),
	(
		"Jika harus tinggal jauh dari orang-orang yang kamu kenal, hal pertama yang kamu pikirkan adalah...",
		[
			Answer("Bagaimana membuat rutinitas dan tempat baru terasa stabil.", {"disiplin": 2, "tenang": 2}),
			Answer("Bagaimana mendapatkan teman dan jaringan baru.", {"sosial": 3}),
			Answer("Hal-hal baru apa yang bisa saya coba.", {"spontan": 3}),
			Answer("Bagaimana tetap bebas mengatur hidup sendiri.", {"mandiri": 3}),
		],
	),
	(
		"Ketika harus menjaga seseorang yang lebih lemah darimu, kamu...",
		[
			Answer("Membuat rencana perlindungan yang matang.", {"logis": 2, "disiplin": 2}),
			Answer("Berdiri di depan dan menghadapi ancaman langsung.", {"berani": 3}),
			Answer("Memastikan ia merasa aman dan didengar.", {"empati": 3}),
			Answer("Mengajarinya agar suatu hari bisa mandiri.", {"mandiri": 2, "ambisius": 1}),
		],
	),
	(
		"Bagaimana kamu menghadapi rutinitas yang wajib dilakukan setiap hari?",
		[
			Answer("Saya membuatnya menjadi kebiasaan yang teratur.", {"disiplin": 3}),
			Answer("Saya mencari alasan yang membuatnya tetap bermakna.", {"ambisius": 2, "empati": 1}),
			Answer("Saya menyisipkan variasi agar tidak membosankan.", {"spontan": 3}),
			Answer("Saya menyelesaikannya secepat mungkin agar punya waktu sendiri.", {"mandiri": 2, "logis": 1}),
		],
	),
	(
		"Ketika seseorang memberi pujian yang tidak kamu sangka, kamu...",
		[
			Answer("Menerimanya dengan tenang dan mengingat alasannya.", {"tenang": 2, "logis": 1}),
			Answer("Membalas dengan pujian atau candaan.", {"sosial": 2, "humoris": 2}),
			Answer("Menjadikannya motivasi untuk bekerja lebih baik.", {"ambisius": 3}),
			Answer("Merasa sedikit canggung tetapi menghargai ketulusannya.", {"empati": 2, "mandiri": 1}),
		],
	),
	(
		"Apa yang kamu lakukan ketika dua orang penting bagimu sedang bertengkar?",
		[
			Answer("Mencari fakta dan membantu mereka melihat masalahnya.", {"logis": 3}),
			Answer("Mendengarkan keduanya tanpa memihak.", {"empati": 3, "tenang": 1}),
			Answer("Mendorong mereka bicara langsung dan menyelesaikannya.", {"berani": 2, "sosial": 1}),
			Answer("Memberi ruang sampai emosi mereka mereda.", {"tenang": 3, "mandiri": 1}),
		],
	),
	(
		"Jika harus memilih pekerjaan, faktor terpenting bagimu adalah...",
		[
			Answer("Kesempatan memecahkan masalah yang menantang.", {"logis": 3}),
			Answer("Dampak nyata bagi kehidupan orang lain.", {"empati": 3}),
			Answer("Peluang berkembang dan mencapai posisi tinggi.", {"ambisius": 3}),
			Answer("Kebebasan menentukan cara dan waktu bekerja.", {"mandiri": 3}),
		],
	),
	(
		"Saat menghadapi orang yang sangat keras kepala, strategi kamu adalah...",
		[
			Answer("Menggunakan fakta dan pertanyaan yang membuatnya berpikir.", {"logis": 3}),
			Answer("Mencari kebutuhan emosional di balik sikapnya.", {"empati": 3}),
			Answer("Menetapkan batas dengan tegas.", {"berani": 3, "disiplin": 1}),
			Answer("Mengubah pendekatan atau menunggu waktu yang lebih tepat.", {"spontan": 2, "tenang": 2}),
		],
	),
	(
		"Seberapa penting memiliki rahasia atau ruang pribadi?",
		[
			Answer("Penting untuk memulihkan pikiran dan menjaga keseimbangan.", {"tenang": 3}),
			Answer("Penting karena saya ingin menentukan apa yang boleh diketahui orang lain.", {"mandiri": 3}),
			Answer("Tidak terlalu penting selama orang dekat memahami saya.", {"sosial": 2, "empati": 1}),
			Answer("Menarik, karena rahasia membuat hidup terasa lebih seru.", {"spontan": 2, "humoris": 1}),
		],
	),
	(
		"Ketika impianmu bertentangan dengan harapan keluarga atau teman, kamu...",
		[
			Answer("Membicarakan alasan dan mencari jalan yang realistis.", {"logis": 2, "empati": 1}),
			Answer("Tetap mengejarnya walaupun harus menanggung risiko sosial.", {"mandiri": 2, "berani": 2}),
			Answer("Menunda sampai bisa membuktikan bahwa pilihanmu masuk akal.", {"disiplin": 2, "ambisius": 2}),
			Answer("Mencari bentuk impian yang bisa melibatkan mereka.", {"sosial": 2, "empati": 2}),
		],
	),
	(
		"Setelah menyelesaikan masalah besar, apa yang paling mungkin kamu lakukan?",
		[
			Answer("Mengevaluasi proses agar kesalahan tidak berulang.", {"logis": 3, "disiplin": 1}),
			Answer("Merayakannya bersama orang-orang yang membantu.", {"sosial": 3, "humoris": 1}),
			Answer("Segera mencari tantangan berikutnya.", {"ambisius": 3, "berani": 1}),
			Answer("Menikmati waktu tenang untuk memulihkan diri.", {"tenang": 3}),
		],
	),
	(
		"Apa yang paling menggambarkan cara kamu mempercayai orang?",
		[
			Answer("Kepercayaan dibangun dari konsistensi dan bukti.", {"logis": 2, "disiplin": 2}),
			Answer("Saya percaya jika merasa ada ketulusan emosional.", {"empati": 3}),
			Answer("Saya memberi kesempatan sampai mereka mengecewakan saya.", {"berani": 2, "spontan": 1}),
			Answer("Saya lebih nyaman mengandalkan diri sendiri.", {"mandiri": 3}),
		],
	),
	(
		"Jika hidupmu berjalan terlalu mudah, kamu mungkin akan...",
		[
			Answer("Mencari proyek intelektual yang menantang.", {"logis": 3, "ambisius": 1}),
			Answer("Mencari cara membantu orang yang belum seberuntung itu.", {"empati": 3}),
			Answer("Menciptakan tantangan atau petualangan baru.", {"spontan": 3, "berani": 1}),
			Answer("Menikmati kedamaian karena itu juga sebuah pencapaian.", {"tenang": 3}),
		],
	),
	(
		"Ketika harus memilih satu hal untuk dipertahankan sepanjang hidup, kamu memilih...",
		[
			Answer("Kemampuan untuk terus memahami dunia.", {"logis": 3, "ambisius": 1}),
			Answer("Orang-orang yang membuat hidup terasa berarti.", {"empati": 3, "sosial": 1}),
			Answer("Kebebasan untuk menentukan pilihan sendiri.", {"mandiri": 3, "berani": 1}),
			Answer("Ketenangan dan kendali atas kehidupan sehari-hari.", {"tenang": 2, "disiplin": 2}),
		],
	),
]


QUESTIONS = QUESTIONS[:40]


def choose_gender():
	print("Pilih gender kamu:")
	print("1. Laki-laki")
	print("2. Perempuan")
	while True:
		choice = input("Pilihan (1/2): ").strip()
		if choice in ("1", "2"):
			return "laki-laki" if choice == "1" else "perempuan"
		print("Pilihan tidak valid. Masukkan 1 atau 2.")


def run_test():
	scores = {trait: 0 for trait in {
		trait for _, answers in QUESTIONS for answer in answers for trait in answer.traits
	}}

	for number, (question, answers) in enumerate(QUESTIONS, start=1):
		print(f"\n{number}/{len(QUESTIONS)}. {question}")
		for option_number, answer in enumerate(answers, start=1):
			print(f"  {option_number}. {answer.text}")
		while True:
			choice = input("Jawaban (1-4): ").strip()
			if choice in {"1", "2", "3", "4"}:
				selected = answers[int(choice) - 1]
				for trait, value in selected.traits.items():
					scores[trait] += value
				break
			print("Pilihan tidak valid. Masukkan angka 1 sampai 4.")
	return scores


def explain_traits(traits, limit=3):
	parts = []
	for trait, _ in sorted(traits.items(), key=lambda item: item[1], reverse=True)[:limit]:
		details = TRAIT_DETAILS.get(trait, {})
		parts.append(details.get('label', trait))
	return ", ".join(parts)


def build_profile_analysis(profile):
	traits = profile.get("traits", {})
	ordered = sorted(traits.items(), key=lambda item: item[1], reverse=True)
	strengths = "; ".join(
		TRAIT_DETAILS.get(trait, {}).get("strength", trait)
		for trait, _ in ordered[:3]
	)
	blind_spot = TRAIT_DETAILS.get(ordered[-1][0], {}).get("risk", "perlu menjaga keseimbangan diri")

	if traits.get("sosial", 0) + traits.get("empati", 0) >= traits.get("mandiri", 0) * 2:
		relationship = "Dalam hubungan, ia cenderung hangat, responsif, dan mudah membaca kebutuhan orang lain."
	elif traits.get("mandiri", 0) >= traits.get("sosial", 0) + 2:
		relationship = "Dalam hubungan, ia menghargai ruang pribadi dan menunjukkan kepedulian lewat tindakan nyata."
	else:
		relationship = "Dalam hubungan, ia menjaga keseimbangan antara kedekatan, kebebasan, dan batas pribadi."

	if traits.get("logis", 0) >= traits.get("spontan", 0) + 2:
		decision_style = "Saat mengambil keputusan, ia mengutamakan data, pola, dan konsekuensi jangka panjang."
	elif traits.get("spontan", 0) >= traits.get("logis", 0) + 2:
		decision_style = "Saat mengambil keputusan, ia mengandalkan intuisi, momentum, dan kemampuan beradaptasi."
	else:
		decision_style = "Saat mengambil keputusan, ia menyeimbangkan pertimbangan rasional dengan intuisi pribadi."

	if traits.get("tenang", 0) + traits.get("disiplin", 0) >= traits.get("berani", 0) + 3:
		pressure_style = "Di bawah tekanan, ia cenderung memperlambat langkah, menyusun prioritas, lalu bergerak terukur."
	else:
		pressure_style = "Di bawah tekanan, ia cenderung bergerak cepat dan memakai tantangan sebagai dorongan untuk bertindak."

	return (
		f"{profile.get('description', 'Profil kepribadian belum tersedia.')} "
		f"Pusat kepribadiannya adalah {explain_traits(dict(ordered), 3)}. "
		f"Kekuatan utamanya: {strengths}. "
		f"{relationship} {decision_style} {pressure_style} "
		f"Hal yang perlu dijaga: {blind_spot}."
	)


def find_matches(scores, gender):
	target_gender = "laki-laki" if gender == "perempuan" else "perempuan"
	max_scores = {
		trait: sum(max(answer.traits.get(trait, 0) for answer in answers) for _, answers in QUESTIONS)
		for trait in scores
	}
	matches = []
	for name, profile in CHARACTER_PROFILES.items():
		if profile.get("gender") != target_gender:
			continue
		similarity = sum(
			(scores.get(trait, 0) / max_scores.get(trait, 1)) * value
			for trait, value in profile.get("traits", {}).items()
		)
		matches.append((similarity, name, profile))
	return sorted(matches, reverse=True)


def show_result(scores, gender):
	print("\n" + "=" * 50)
	print("HASIL TES")
	print("=" * 50)
	print(f"Gender: {gender}")
	top_traits = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:3]
	print("Trait paling dominan: " + explain_traits(dict(top_traits)))
	print("\nPembacaan singkat kepribadianmu:")
	for trait, _ in top_traits:
		info = TRAIT_DETAILS.get(trait, {})
		print(f"- {info.get('label', trait)}: {info.get('strength', 'trait utama dalam jawabanmu')}.")

	matches = find_matches(scores, gender)
	if not matches:
		print("\nBelum ada karakter dengan gender yang sesuai.")
		return

	target_gender = "laki-laki" if gender == "perempuan" else "perempuan"
	print(f"\nKarakter {target_gender} yang paling cocok denganmu:")
	for similarity, name, profile in matches[:3]:
		print(f"\n- {name} (skor kecocokan {similarity:.2f})")
		print(f"  Trait inti: {explain_traits(profile.get('traits', {}), 4)}")
		print(f"  {build_profile_analysis(profile)}")


def main():
	print("TES KECOCOKAN KARAKTER HONKAI: STAR RAIL")
	print(f"Jawab {len(QUESTIONS)} pertanyaan sesuai dirimu, bukan jawaban yang ideal.\n")
	gender = choose_gender()
	scores = run_test()
	show_result(scores, gender)


if __name__ == "__main__":
	main()

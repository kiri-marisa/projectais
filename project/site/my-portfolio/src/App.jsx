import React from "react";

const styles = {
  page: {
    minHeight: "100vh",
    background:
      "radial-gradient(circle at top left, rgba(99,102,241,0.22), transparent 28%), radial-gradient(circle at top right, rgba(56,189,248,0.18), transparent 22%), linear-gradient(180deg, #0b1020 0%, #11162a 45%, #0b1020 100%)",
    color: "#f8fafc",
    fontFamily:
      'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    overflowX: "hidden",
  },
  container: {
    width: "min(1380px, calc(100% - 96px))",
    margin: "0 auto",
  },
  nav: {
    position: "sticky",
    top: 0,
    zIndex: 20,
    backdropFilter: "blur(18px)",
    background: "rgba(11, 16, 32, 0.82)",
    borderBottom: "1px solid rgba(148, 163, 184, 0.08)",
  },
  navInner: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    gap: 20,
    padding: "18px 0",
    flexWrap: "wrap",
  },
  brandTitle: {
    fontSize: 22,
    fontWeight: 700,
    letterSpacing: "-0.04em",
    margin: 0,
  },
  brandText: {
    margin: "2px 0 0",
    color: "#dbeafe",
    fontSize: 14,
  },
  links: {
    display: "flex",
    gap: 18,
    flexWrap: "wrap",
  },
  link: {
    color: "#e2e8f0",
    textDecoration: "none",
    fontSize: 15,
  },
  hero: {
    padding: "72px 0 40px",
  },
  heroGrid: {
    display: "grid",
    gridTemplateColumns: "1.15fr 0.85fr",
    gap: 36,
    alignItems: "center",
  },
  badge: {
    display: "inline-flex",
    padding: "10px 16px",
    borderRadius: 999,
    background: "rgba(59, 130, 246, 0.12)",
    border: "1px solid rgba(96, 165, 250, 0.24)",
    color: "#93c5fd",
    fontSize: 14,
    marginBottom: 20,
  },
  title: {
    fontSize: "clamp(42px, 7vw, 78px)",
    lineHeight: 0.95,
    letterSpacing: "-0.06em",
    margin: 0,
    maxWidth: 760,
  },
  lead: {
    fontSize: 18,
    lineHeight: 1.75,
    color: "#cbd5e1",
    marginTop: 24,
    maxWidth: 620,
  },
  actions: {
    display: "flex",
    gap: 14,
    flexWrap: "wrap",
    marginTop: 30,
  },
  buttonPrimary: {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "14px 22px",
    borderRadius: 16,
    background: "linear-gradient(135deg, #60a5fa, #6366f1)",
    color: "white",
    fontWeight: 700,
    textDecoration: "none",
    boxShadow: "0 18px 40px rgba(37, 99, 235, 0.25)",
  },
  buttonGhost: {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "14px 22px",
    borderRadius: 16,
    border: "1px solid rgba(148, 163, 184, 0.22)",
    color: "#e2e8f0",
    textDecoration: "none",
    background: "rgba(255,255,255,0.03)",
  },
  panel: {
    background: "linear-gradient(180deg, rgba(15,23,42,0.92), rgba(15,23,42,0.78))",
    border: "1px solid rgba(148, 163, 184, 0.08)",
    borderRadius: 28,
    boxShadow: "0 30px 80px rgba(2, 6, 23, 0.34)",
  },
  heroCard: {
    padding: 26,
    position: "relative",
    overflow: "hidden",
  },
  glow: {
    position: "absolute",
    inset: "auto -50px -60px auto",
    width: 180,
    height: 180,
    borderRadius: "50%",
    background: "radial-gradient(circle, rgba(99,102,241,0.38), transparent 65%)",
  },
  profileTop: {
    display: "flex",
    alignItems: "center",
    gap: 14,
  },
  avatar: {
    width: 58,
    height: 58,
    borderRadius: 18,
    background: "linear-gradient(135deg, #60a5fa, #818cf8)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontWeight: 800,
    fontSize: 22,
  },
  muted: {
    color: "#dbeafe",
  },
  statGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(2, minmax(0, 1fr))",
    gap: 14,
    marginTop: 24,
  },
  statCard: {
    padding: 18,
    borderRadius: 20,
    background: "rgba(255,255,255,0.04)",
    border: "1px solid rgba(148, 163, 184, 0.08)",
  },
  section: {
    padding: "26px 0",
  },
  sectionTitle: {
    fontSize: 34,
    margin: "0 0 12px",
    letterSpacing: "-0.04em",
  },
  sectionLead: {
    color: "#dbeafe",
    lineHeight: 1.7,
    maxWidth: 700,
    marginBottom: 24,
  },
  aboutGrid: {
    display: "grid",
    gridTemplateColumns: "1.12fr 0.88fr",
    gap: 28,
  },
  cardPadding: {
    padding: 28,
  },
  chipWrap: {
    display: "flex",
    flexWrap: "wrap",
    gap: 12,
    marginTop: 18,
  },
  chip: {
    padding: "10px 14px",
    borderRadius: 999,
    background: "rgba(30, 41, 59, 0.95)",
    border: "1px solid rgba(148, 163, 184, 0.12)",
    color: "#e2e8f0",
    fontSize: 14,
  },
  projectsGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
    gap: 26,
  },
  projectCard: {
    padding: 22,
    borderRadius: 26,
    background: "linear-gradient(180deg, rgba(15,23,42,0.9), rgba(15,23,42,0.76))",
    border: "1px solid rgba(148, 163, 184, 0.08)",
    boxShadow: "0 16px 40px rgba(2, 6, 23, 0.22)",
  },
  projectPreview: {
    height: 190,
    borderRadius: 22,
    background:
      "linear-gradient(135deg, rgba(96,165,250,0.28), rgba(99,102,241,0.2)), linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01))",
    border: "1px solid rgba(148, 163, 184, 0.08)",
    display: "flex",
    alignItems: "end",
    padding: 18,
    marginBottom: 18,
  },
  timeline: {
    display: "grid",
    gap: 16,
  },
  timelineItem: {
    padding: 24,
    borderRadius: 24,
    background: "rgba(15, 23, 42, 0.88)",
    border: "1px solid rgba(148, 163, 184, 0.08)",
  },
  contactBox: {
    padding: 30,
    borderRadius: 30,
    background:
      "linear-gradient(135deg, rgba(59,130,246,0.12), rgba(99,102,241,0.12)), rgba(15,23,42,0.9)",
    border: "1px solid rgba(96, 165, 250, 0.1)",
  },
  contactRow: {
    display: "flex",
    gap: 14,
    flexWrap: "wrap",
    marginTop: 22,
  },
  contactItem: {
    padding: "14px 18px",
    borderRadius: 16,
    textDecoration: "none",
    color: "#f8fafc",
    background: "rgba(255,255,255,0.04)",
    border: "1px solid rgba(148, 163, 184, 0.12)",
  },
  footer: {
    padding: "20px 0 42px",
    color: "#94a3b8",
    fontSize: 14,
  },
};

const skills = [
  "Python",
  "C++",
  "HTML",
  "JavaScript (basic)",
  "React",
  "Docker",
  "Web basics",
  "Responsive Layout",
];

const projects = [
  {
    title: "Игра «Змейка»",
    description:
      "Небольшая игра с базовой игровой логикой, обработкой столкновений, подсчётом очков и простой визуальной подачей.",
    stack: ["Python", "Game Logic", "UI basics"],
  },
  {
    title: "Распознавание лиц",
    description:
      "Учебный проект по распознаванию лиц на изображении или видеопотоке с использованием готовых библиотек компьютерного зрения.",
    stack: ["Python", "OpenCV", "Computer Vision"],
  },
  {
    title: "Практика с вёрсткой",
    description:
      "Разбор структуры разных сайтов, работа с HTML-разметкой, стилями и базовыми интерактивными элементами на JavaScript.",
    stack: ["HTML", "CSS", "JavaScript"],
  },
];

const experience = [
  {
    period: "2024 — настоящее время",
    role: "Разработка учебных проектов",
    place: "Личные и учебные задачи",
    description:
      "Пишу программы на Python и C++, делаю небольшие игровые проекты, изучаю фронтенд и пробую разные подходы к созданию веб-страниц.",
  },
  {
    period: "2023 — 2024",
    role: "Практика с вебом и контейнерами",
    place: "Самостоятельное обучение",
    description:
      "Работал с HTML-структурой сайтов, немного с JavaScript, изучал Docker и интересовался основами веб-безопасности в учебной среде.",
  },
];

function SectionTitle({ eyebrow, title, text }) {
  return (
    <div style={{ marginBottom: 22 }}>
      {eyebrow ? (
        <div
          style={{
            textTransform: "uppercase",
            letterSpacing: "0.18em",
            color: "#93c5fd",
            fontSize: 12,
            marginBottom: 10,
          }}
        >
          {eyebrow}
        </div>
      ) : null}
      <h2 style={styles.sectionTitle}>{title}</h2>
      {text ? <p style={styles.sectionLead}>{text}</p> : null}
    </div>
  );
}

export default function PortfolioSite() {
  return (
    <div style={styles.page}>
      <div
        style={{
          position: "fixed",
          inset: 0,
          pointerEvents: "none",
          background:
            "linear-gradient(90deg, #0b1020 0, #0b1020 max(24px, calc((100vw - min(1380px, calc(100vw - 96px))) / 2)), transparent max(24px, calc((100vw - min(1380px, calc(100vw - 96px))) / 2)), transparent calc(100vw - max(24px, calc((100vw - min(1380px, calc(100vw - 96px))) / 2))), #0b1020 calc(100vw - max(24px, calc((100vw - min(1380px, calc(100vw - 96px))) / 2))), #0b1020 100%)",
          zIndex: 0,
        }}
      />
      <header style={{ ...styles.nav, position: "relative", zIndex: 2 }}>
        <div style={styles.container}>
          <div style={styles.navInner}>
            <div>
              <p style={styles.brandTitle}>Халиков Динар</p>
              <p style={styles.brandText}>Python / C++ / Web</p>
            </div>
            <nav style={styles.links}>
              <a href="#about" style={styles.link}>Обо мне</a>
              <a href="#projects" style={styles.link}>Проекты</a>
              <a href="#experience" style={styles.link}>Опыт</a>
              <a href="#contact" style={styles.link}>Контакты</a>
            </nav>
          </div>
        </div>
      </header>

      <main style={{ position: "relative", zIndex: 1 }}>
        <section style={styles.hero}>
          <div style={styles.container}>
            <div className="hero-grid" style={styles.heroGrid}>
              <div>
                <div style={styles.badge}>Python developer · C++ · Web basics</div>
                <h1 style={styles.title}>Пишу программы, делаю учебные игры и изучаю веб-разработку</h1>
                <p style={styles.lead}>
                  Работаю с Python и C++, собираю небольшие проекты, пробую фронтенд,
                  изучаю Docker и развиваюсь в сторону практичной и аккуратной разработки.
                </p>
                <div style={styles.actions}>
                  <a href="#projects" style={styles.buttonPrimary}>Смотреть проекты</a>
                  <a href="#contact" style={styles.buttonGhost}>Написать мне</a>
                </div>
              </div>

              <div style={{ ...styles.panel, ...styles.heroCard }}>
                <div style={styles.glow} />
                <div style={styles.profileTop}>
                  <div
                    style={{
                      width: 72,
                      height: 72,
                      borderRadius: 22,
                      overflow: "hidden",
                      background: "linear-gradient(135deg, #60a5fa, #818cf8)",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      flexShrink: 0,
                    }}
                  >
                    <img
                      src="/avatar.jpg"
                      alt="Фото профиля"
                      style={{ width: "100%", height: "100%", objectFit: "cover" }}
                      onError={(e) => {
                        e.currentTarget.style.display = "none";
                        const next = e.currentTarget.nextElementSibling;
                        if (next) next.style.display = "flex";
                      }}
                    />
                    <div style={{ ...styles.avatar, display: "none", width: "100%", height: "100%", borderRadius: 0 }}>ДХ</div>
                  </div>
                  <div>
                    <div style={{ fontSize: 22, fontWeight: 700 }}>Халиков Динар</div>
                    <div style={{ ...styles.muted, marginTop: 4 }}>Python / C++ / Web basics</div>
                  </div>
                </div>

                <div style={styles.statGrid}>
                  <div style={styles.statCard}>
                    <div style={styles.muted}>Проектов</div>
                    <div style={{ marginTop: 8, fontSize: 26, fontWeight: 700 }}>5+</div>
                  </div>
                  <div style={styles.statCard}>
                    <div style={styles.muted}>Опыт</div>
                    <div style={{ marginTop: 8, fontSize: 26, fontWeight: 700 }}>1+ год</div>
                  </div>
                  <div style={styles.statCard}>
                    <div style={styles.muted}>Основной стек</div>
                    <div style={{ marginTop: 8, fontSize: 20, fontWeight: 700 }}>Python</div>
                  </div>
                  <div style={styles.statCard}>
                    <div style={styles.muted}>Фокус</div>
                    <div style={{ marginTop: 8, fontSize: 20, fontWeight: 700 }}>Backend / Web</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="about" style={styles.section}>
          <div style={styles.container}>
            <div className="about-grid" style={styles.aboutGrid}>
              <div style={{ ...styles.panel, ...styles.cardPadding }}>
                <SectionTitle
                  eyebrow="Обо мне"
                  title="Практика в программировании, играх и изучении веб-разработки"
                  text="Мне интересно развиваться сразу в нескольких направлениях: программирование на Python и C++, учебные игровые проекты, основы фронтенда и работа с контейнерами."
                />
                <p style={{ color: "#cbd5e1", lineHeight: 1.8, margin: 0 }}>
                  Сейчас я развиваю навыки backend- и frontend-разработки, пишу небольшие программы,
                  делаю учебные игры вроде змейки и тетриса, изучаю Docker и лучше понимаю,
                  как устроены современные веб-проекты и вопросы их безопасности.
                </p>
              </div>

              <div style={{ ...styles.panel, ...styles.cardPadding }}>
                <SectionTitle title="Навыки" text="Технологии и инструменты, с которыми я работаю." />
                <div style={styles.chipWrap}>
                  {skills.map((skill) => (
                    <span key={skill} style={styles.chip}>{skill}</span>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="projects" style={styles.section}>
          <div style={styles.container}>
            <SectionTitle
              eyebrow="Portfolio"
              title="Учебные проекты"
              text="Здесь собраны проекты, на которых я отрабатывал игровую логику, базовую веб-разработку и навыки программирования."
            />
            <div className="projects-grid" style={styles.projectsGrid}>
              {projects.map((project, index) => (
                <article key={project.title} style={styles.projectCard}>
                  <div style={styles.projectPreview}>
                    <div>
                      <div style={{ fontSize: 12, color: "#bfdbfe", letterSpacing: "0.12em", textTransform: "uppercase" }}>
                        0{index + 1}
                      </div>
                      <div style={{ fontSize: 22, fontWeight: 700, marginTop: 8 }}>{project.title}</div>
                    </div>
                  </div>
                  <p style={{ color: "#cbd5e1", lineHeight: 1.7, minHeight: 82 }}>{project.description}</p>
                  <div style={styles.chipWrap}>
                    {project.stack.map((item) => (
                      <span key={item} style={{ ...styles.chip, fontSize: 13 }}>{item}</span>
                    ))}
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section id="experience" style={styles.section}>
          <div style={styles.container}>
            <SectionTitle
              eyebrow="Опыт"
              title="Практика и развитие навыков"
              text="Мой опыт строится вокруг учебных задач, самостоятельной практики и постепенного изучения разработки и инфраструктуры."
            />
            <div style={styles.timeline}>
              {experience.map((item) => (
                <div key={item.role + item.period} style={styles.timelineItem}>
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      gap: 16,
                      alignItems: "flex-start",
                      flexWrap: "wrap",
                    }}
                  >
                    <div>
                      <div style={{ fontSize: 22, fontWeight: 700 }}>{item.role}</div>
                      <div style={{ ...styles.muted, marginTop: 6 }}>{item.place}</div>
                    </div>
                    <div style={{ color: "#93c5fd", fontWeight: 600 }}>{item.period}</div>
                  </div>
                  <p style={{ color: "#cbd5e1", lineHeight: 1.8, margin: "14px 0 0" }}>{item.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="contact" style={styles.section}>
          <div style={styles.container}>
            <div style={styles.contactBox}>
              <SectionTitle
                eyebrow="Контакты"
                title="Готов обсудить проект или стажировку"
                text="Открыт к сотрудничеству, учебным и коммерческим задачам, а также к предложениям по практике."
              />
              <div style={styles.contactRow}>
                <a href="mailto:nefordina@gmail.com" style={styles.contactItem}>nefordina@gmail.com</a>
                <a href="tel:+79297588058" style={styles.contactItem}>+7 (929) 758-80-58</a>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer style={styles.footer}>
        <div style={styles.container}>© 2026 Халиков Динар. Portfolio website.</div>
      </footer>

      <style>{`
        * { box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { margin: 0; background: #0b1020; }
        a { transition: 0.2s ease; }
        a:hover { transform: translateY(-1px); opacity: 0.96; }
        h1, h2, h3, p, a, span, div { color: inherit; }

        @media (min-width: 1400px) {
          .hero-grid {
            grid-template-columns: minmax(0, 1.1fr) minmax(360px, 420px) !important;
          }
        }

        @media (max-width: 960px) {
          .hero-grid,
          .about-grid,
          .projects-grid {
            grid-template-columns: 1fr !important;
          }
        }
      `}</style>
    </div>
  );
}

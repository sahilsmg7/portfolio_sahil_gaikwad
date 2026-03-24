import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Sahil Gaikwad - Material Portfolio</title>
    <link rel="stylesheet" href="style.css" />
    <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <a href="#" class="logo">SAHIL</a>
        <nav class="navbar">
            <a href="#home" class="active">Home</a>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>

    <section class="home" id="home">
        <div class="md-card hero-card">
            <div class="hero-chip">Hello, It's Me</div>
            <h1 class="hero-title">SAHIL GAIKWAD</h1>
            <h3 class="hero-subtitle">Java Full Stack Developer</h3>
            <p class="hero-text">
                Computer Engineering graduate with a strong foundation in Java Full-Stack Development and professional experience. Proven ability to build scalable apps and manage complex data systems.
            </p>
            <div class="social-fab-container">
                <a href="https://github.com/sahilsmg7" class="md-fab"><i class="bx bxl-github"></i></a>
                <a href="https://instagram.com/sahilgaikwad07_" class="md-fab"><i class="bx bxl-instagram"></i></a>
                <a href="https://www.linkedin.com/in/sahil-gaikwad-8811b6171" class="md-fab"><i class="bx bxl-linkedin"></i></a>
            </div>
            <a href="Sahil_Gaikwad_Resume.pdf" download="Sahil_Gaikwad_Resume.pdf" class="md-btn md-btn-primary">DOWNLOAD RESUME</a>
        </div>
    </section>

    <section class="about section-padding" id="about">
        <h2 class="section-title">About <span>Me</span></h2>
        <div class="md-card about-card">
            <h4>WNS Global Services - Associate in Operations</h4>
            <p>Managed billing processes using IBM i (AS/400) systems. Maintained high accuracy in data operations and documentation. Collaborated with global teams to ensure timely delivery of service goals.</p>
            <hr class="md-divider"/>
            <div class="education-grid">
                <div>
                    <h5>B.E. Computer Engineering</h5>
                    <p>Savitribai Phule Pune University<br/>72.20% | 2021-2024</p>
                </div>
                <div>
                    <h5>Diploma In Computer Engineering</h5>
                    <p>Met's Institute Of Polytechnic Nashik<br/>85.71% | 2018-2021</p>
                </div>
            </div>
        </div>
    </section>

    <section class="skills section-padding" id="skills">
        <h2 class="section-title">My <span>Skills</span></h2>
        <div class="skills-grid">
            <div class="md-card skill-card">
                <i class="bx bxl-java" style="color: #ea4335;"></i>
                <h3>Java (Core & Advanced)</h3>
                <div class="md-progress-track"><div class="md-progress-fill" style="width: 85%; background: #ea4335;"></div></div>
            </div>
            <div class="md-card skill-card">
                <i class="bx bx-data" style="color: #fbbc04;"></i>
                <h3>SQL / Oracle</h3>
                <div class="md-progress-track"><div class="md-progress-fill" style="width: 80%; background: #fbbc04;"></div></div>
            </div>
            <div class="md-card skill-card">
                <i class="bx bx-code-alt" style="color: #34a853;"></i>
                <h3>JSP, Servlets & JDBC</h3>
                <div class="md-progress-track"><div class="md-progress-fill" style="width: 90%; background: #34a853;"></div></div>
            </div>
            <div class="md-card skill-card">
                <i class="bx bxl-html5" style="color: #4285f4;"></i>
                <h3>HTML5 & CSS3</h3>
                <div class="md-progress-track"><div class="md-progress-fill" style="width: 95%; background: #4285f4;"></div></div>
            </div>
        </div>
    </section>

    <section class="projects section-padding" id="projects">
        <h2 class="section-title">Featured <span>Projects</span></h2>
        <div class="projects-grid">
            <div class="md-card project-card">
                <div class="project-icon"><i class="bx bx-folder"></i></div>
                <h3>Student Management System</h3>
                <p class="md-chip">Java Full-Stack</p>
                <p>Developed a complete web application with full CRUD functionality using Java, Servlets, JSP, JDBC, and MySQL. Implemented strict session management.</p>
            </div>
            <div class="md-card project-card">
                <div class="project-icon" style="background: #e6f4ea; color: #1e8e3e;"><i class="bx bx-wallet"></i></div>
                <h3>Smart Bank Transaction</h3>
                <p class="md-chip">Backend Developer</p>
                <p>Built transaction logic to handle deposits and withdrawals. Leveraged HashMaps for O(1) time complexity in account retrieval and custom Exception Handling.</p>
            </div>
            <div class="md-card project-card">
                <div class="project-icon" style="background: #fce8e6; color: #d93025;"><i class="bx bx-car"></i></div>
                <h3>Vehicle Service System</h3>
                <p class="md-chip">Java Developer</p>
                <p>Designed a logic-heavy system to automate maintenance schedules. Applied Encapsulation to secure customer data and Inheritance to manage vehicle types.</p>
            </div>
        </div>
    </section>

    <section class="contact section-padding" id="contact">
        <h2 class="section-title">Contact <span>Me</span></h2>
        <div class="contact-layout">
            <div class="md-card contact-info">
                <h3>Let's Work Together</h3>
                <p>Reach out and let's craft amazing software together!</p>
                <ul>
                    <li><i class="bx bxs-envelope"></i> sahilgaikwad2002official@gmail.com</li>
                    <li><i class="bx bx-phone"></i> +91 9168073559</li>
                </ul>
            </div>
            <div class="md-card contact-form">
                <form>
                    <div class="md-input-group">
                        <input type="text" required />
                        <label>Your Name</label>
                    </div>
                    <div class="md-input-group">
                        <input type="email" required />
                        <label>Your Email</label>
                    </div>
                    <div class="md-input-group">
                        <textarea required rows="4"></textarea>
                        <label>Your Message</label>
                    </div>
                    <button class="md-btn md-btn-primary" type="submit">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <p>Developed with ❤️ and Material Design by Sahil Gaikwad</p>
    </footer>

    <script src="main.js"></script>
</body>
</html>
"""

css_content = """* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Roboto', sans-serif; scroll-behavior: smooth; }

:root {
    --md-sys-color-primary: #0b57d0;
    --md-sys-color-on-primary: #ffffff;
    --md-sys-color-primary-container: #d3e3fd;
    --md-sys-color-on-primary-container: #041e49;
    
    --md-sys-color-background: #f5f7f8;
    --md-sys-color-surface: #ffffff;
    --md-sys-color-surface-variant: #e1e3e1;
    --md-sys-color-on-surface: #1f1f1f;
    --md-sys-color-on-surface-variant: #444746;
    
    --md-elevation-1: 0px 1px 2px 0px rgba(0, 0, 0, 0.3), 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
    --md-elevation-2: 0px 1px 2px 0px rgba(0, 0, 0, 0.3), 0px 2px 6px 2px rgba(0, 0, 0, 0.15);
    --md-elevation-3: 0px 1px 3px 0px rgba(0, 0, 0, 0.3), 0px 4px 8px 3px rgba(0, 0, 0, 0.15);
    
    --md-shape-corner-extra-large: 32px;
    --md-shape-corner-large: 16px;
    --md-shape-corner-full: 100px;
}

body {
    background-color: var(--md-sys-color-background);
    color: var(--md-sys-color-on-surface);
    line-height: 1.5;
}

.section-padding { padding: 80px 10%; }
.section-title { font-size: 36px; font-weight: 500; text-align: center; margin-bottom: 40px; }
.section-title span { color: var(--md-sys-color-primary); }

/* Buttons & Chips */
.md-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 48px;
    padding: 0 32px;
    border-radius: var(--md-shape-corner-full);
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s ease;
    border: none;
    cursor: pointer;
    font-size: 15px;
    letter-spacing: 0.5px;
}

.md-btn-primary {
    background-color: var(--md-sys-color-primary);
    color: var(--md-sys-color-on-primary);
}

.md-btn-primary:hover {
    box-shadow: var(--md-elevation-2);
    background-color: #0842a0;
}

.md-fab {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 64px;
    height: 64px;
    border-radius: var(--md-shape-corner-large);
    background-color: var(--md-sys-color-primary-container);
    color: var(--md-sys-color-on-primary-container);
    font-size: 28px;
    box-shadow: var(--md-elevation-1);
    text-decoration: none;
    transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.md-fab:hover {
    box-shadow: var(--md-elevation-3);
    transform: translateY(-2px);
}

.md-chip {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 8px;
    background-color: var(--md-sys-color-surface-variant);
    color: var(--md-sys-color-on-surface-variant);
    font-size: 12px;
    font-weight: 500;
    margin-bottom: 12px;
}

/* Cards */
.md-card {
    background-color: var(--md-sys-color-surface);
    border-radius: var(--md-shape-corner-extra-large);
    padding: 32px;
    box-shadow: var(--md-elevation-1);
    transition: box-shadow 0.2s ease;
}
.md-card:hover { box-shadow: var(--md-elevation-2); }

.md-divider { border: 0; height: 1px; background: var(--md-sys-color-surface-variant); margin: 24px 0; }

/* Header */
.header {
    position: fixed;
    top: 0; left: 0; width: 100%;
    padding: 20px 5%;
    background-color: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
    box-shadow: var(--md-elevation-1);
}

.logo {
    font-size: 24px;
    font-weight: 700;
    color: var(--md-sys-color-primary);
    text-decoration: none;
}

.navbar a {
    color: var(--md-sys-color-on-surface-variant);
    text-decoration: none;
    font-weight: 500;
    margin-left: 24px;
    padding: 10px 20px;
    border-radius: var(--md-shape-corner-full);
    transition: background-color 0.2s ease, color 0.2s ease;
}

.navbar a:hover, .navbar a.active {
    background-color: var(--md-sys-color-primary-container);
    color: var(--md-sys-color-on-primary-container);
}

/* Home */
.home {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-top: 80px;
    background: radial-gradient(circle at top center, #e8f0fe, #f5f7f8);
}
.hero-card {
    max-width: 800px;
    text-align: center;
    padding: 56px 40px;
}
.hero-chip {
    display: inline-block;
    padding: 8px 20px;
    border-radius: 100px;
    background: #e8f0fe;
    color: #1967d2;
    font-weight: 500;
    margin-bottom: 24px;
    font-size: 14px;
}
.hero-title { font-size: 64px; font-weight: 300; color: var(--md-sys-color-on-surface); margin-bottom: 8px; letter-spacing: -1.5px; }
.hero-subtitle { font-size: 26px; color: var(--md-sys-color-on-surface-variant); margin-bottom: 24px; font-weight: 400; }
.hero-text { font-size: 18px; color: var(--md-sys-color-on-surface-variant); margin-bottom: 40px; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.6; }
.social-fab-container { display: flex; gap: 24px; justify-content: center; margin-bottom: 40px; }

/* About Grid */
.about-card { max-width: 900px; margin: 0 auto; }
.about-card h4 { font-size: 20px; font-weight: 500; margin-bottom: 12px; }
.about-card p { font-size: 16px; color: var(--md-sys-color-on-surface-variant); }
.education-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.education-grid h5 { font-size: 18px; font-weight: 500; margin-bottom: 8px; }

/* Skills Grid */
.skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px; max-width: 1000px; margin: 0 auto; }
.skill-card { display: flex; flex-direction: column; align-items: flex-start; }
.skill-card i { font-size: 40px; margin-bottom: 16px; }
.skill-card h3 { font-size: 18px; font-weight: 500; margin-bottom: 16px; }
.md-progress-track { width: 100%; height: 8px; background: var(--md-sys-color-surface-variant); border-radius: 4px; overflow: hidden; }
.md-progress-fill { height: 100%; border-radius: 4px; }

/* Projects Grid */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; max-width: 1000px; margin: 0 auto; }
.project-card { display: flex; flex-direction: column; align-items: flex-start; }
.project-icon { width: 64px; height: 64px; border-radius: 16px; background: #e8f0fe; color: #1967d2; display: flex; align-items: center; justify-content: center; font-size: 32px; margin-bottom: 24px; }
.project-card h3 { font-size: 22px; font-weight: 500; margin-bottom: 12px; }
.project-card p { color: var(--md-sys-color-on-surface-variant); margin-bottom: 0; font-size: 16px; }

/* Contact Layout */
.contact-layout { display: grid; grid-template-columns: 1fr 1.5fr; gap: 24px; max-width: 900px; margin: 0 auto; }
.contact-info h3 { font-size: 24px; font-weight: 500; margin-bottom: 16px; }
.contact-info p { color: var(--md-sys-color-on-surface-variant); margin-bottom: 24px; }
.contact-info ul { list-style: none; }
.contact-info li { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; color: var(--md-sys-color-on-surface-variant); font-size: 16px; }
.contact-info i { font-size: 24px; color: var(--md-sys-color-primary); }

.md-input-group { position: relative; margin-bottom: 24px; }
.md-input-group input, .md-input-group textarea {
    width: 100%;
    padding: 16px;
    border: 1px solid var(--md-sys-color-surface-variant);
    border-radius: var(--md-shape-corner-large);
    font-size: 16px;
    outline: none;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    background: #fafafa;
}
.md-input-group input:focus, .md-input-group textarea:focus {
    border-color: var(--md-sys-color-primary);
    box-shadow: 0 0 0 2px var(--md-sys-color-primary-container);
}
.md-input-group label {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--md-sys-color-on-surface-variant);
    transition: all 0.2s ease;
    pointer-events: none;
    background: transparent;
    padding: 0 4px;
}
.md-input-group textarea + label { top: 24px; }
.md-input-group input:focus + label, .md-input-group input:valid + label,
.md-input-group textarea:focus + label, .md-input-group textarea:valid + label {
    top: -8px; font-size: 12px; color: var(--md-sys-color-primary); background: #fafafa; border-radius: 4px;
}

.footer { text-align: center; padding: 24px; color: var(--md-sys-color-on-surface-variant); margin-top: 40px; }

@media (max-width: 768px) {
    .contact-layout { grid-template-columns: 1fr; }
    .education-grid { grid-template-columns: 1fr; }
    .hero-title { font-size: 48px; }
    .hero-subtitle { font-size: 20px; }
}
"""

with open('c:/Users/sahil/Anti-Gravity/Youtube Workspace/portfolio_sahil_gaikwad/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('c:/Users/sahil/Anti-Gravity/Youtube Workspace/portfolio_sahil_gaikwad/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Material files rebuilt successfully")

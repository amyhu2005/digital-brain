html_content = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile // Amy Hu</title>
    <link rel="stylesheet" href="style.css">
    <script src="admin.js" defer></script>
    <script src="script.js" defer></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .profile-section-title {
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--text-main);
            border-bottom: 2px solid var(--text-main);
            display: inline-block;
            margin-bottom: 1rem;
            padding-bottom: 2px;
            letter-spacing: -0.01em;
            text-transform: lowercase;
        }

        .profile-list {
            list-style-type: disc;
            padding-left: 1.2rem;
            font-size: 1.05rem;
            line-height: 1.6;
            color: var(--text-main);
        }

        .profile-list li {
            margin-bottom: 0.4rem;
        }

        .profile-list li strong {
            font-weight: 600;
        }
    </style>
</head>

<body>
    <div class="side-id">AMY_HU // PROFILE // 2026.04.30</div>
    <div class="tech-tag vertical" style="top: 50px; left: 20px;">SYSTEM_V2.0.4 // PROFILE_01</div>
    <div class="tech-tag orange" style="top: 20px; right: 20px;">REF_PROFILE</div>

    <nav class="floating-sidebar visible">
        <a href="index.html#bio" class="sidebar-item" data-label="home"><i data-lucide="home"></i></a>
        <a href="profile.html" class="sidebar-item" data-label="profile"><i data-lucide="user"></i></a>
        <a href="4am.html" class="sidebar-item" data-label="vibecoding"><i data-lucide="terminal"></i></a>
        <a href="woodshop.html" class="sidebar-item" data-label="woodworking"><i data-lucide="hammer"></i></a>
        <a href="thoughts.html" class="sidebar-item" data-label="writing"><i data-lucide="pen-tool"></i></a>
        <a href="music.html" class="sidebar-item" data-label="search history"><i data-lucide="search"></i></a>
    </nav>

    <div class="blog-container" style="padding: 100px 2rem 100px 2rem; max-width: 800px; margin: 0 auto; width: 100%;">
        <div class="blog-header" style="margin-bottom: 40px; border-bottom: 1px solid var(--border-color); padding-bottom: 15px;">
            <p class="blog-subtitle" style="margin-bottom: 0; font-size: 1rem;">// IDENT // CORE_PROFILE</p>
        </div>

        <div class="content-body" style="display: flex; flex-direction: column; gap: 40px;">

            <!-- Bio Header -->
            <div style="margin-bottom: 20px;">
                <h2 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 15px; letter-spacing: -0.04em; color: var(--text-main);">Amy Hu</h2>
                <p style="font-size: 1.4rem; font-weight: 400; color: var(--text-main); margin-bottom: 15px;">Bachelors of Economics and Masters of Public Policy</p>
                <p style="font-style: italic; font-size: 1.05rem; color: var(--text-muted);">"AGE 20 // UCSD CLASS OF 2027"</p>
            </div>

            <!-- Location -->
            <div>
                <h3 class="profile-section-title">location:</h3>
                <ul class="profile-list">
                    <li><strong>Currently:</strong> San Diego, CA</li>
                    <li><strong>Summer 2026:</strong> Berlin</li>
                    <li><strong>Home:</strong> Cupertino, CA</li>
                </ul>
            </div>

            <!-- Hats & Work -->
            <div>
                <h3 class="profile-section-title">current hats:</h3>
                <ul class="profile-list">
                    <li><strong>Research Assistant:</strong> Researching Macroeconomic uncertainty shocks</li>
                    <li><strong>Resident Assistant:</strong> UCSD 7th College Resident Life</li>
                    <li><strong>Consultant:</strong> UCSD Global Policy School Consulting</li>
                </ul>
                <div style="margin-top: 15px; padding-left: 1.2rem; font-size: 1.05rem; color: var(--text-main);">
                    <strong style="color: var(--accent-orange);">*</strong> Looking for work in Berlin End of June-Early August 2026 
                    <span style="color: var(--text-muted);">(happy to work extended virtually)</span>
                </div>
            </div>

            <!-- Chipping away -->
            <div>
                <h3 class="profile-section-title">chipping away at:</h3>
                <ul class="profile-list">
                    <li><em>Linear Algebra and Its Applications (4th edition)</em> — <span style="color: var(--accent-orange);">Gilbert Strang</span></li>
                    <li><em>An Introduction to Statistical Reasoning with Application in Python</em> — <span style="color: var(--accent-orange);">Gareth James et al.</span></li>
                    <li><em>Glial Neurobiology</em> — <span style="color: var(--accent-orange);">Alexei Verkhratsky, Arthur Butt</span></li>
                </ul>
            </div>

            <!-- Currently Reading -->
            <div>
                <h3 class="profile-section-title">currently reading:</h3>
                <p style="font-size: 1.05rem; padding-left: 1.2rem; color: var(--text-main);"><em>Cat's Cradle</em> — <span style="color: var(--accent-orange);">Kurt Vonnegut</span></p>
            </div>

            <!-- Obsessions -->
            <div>
                <h3 class="profile-section-title">current obsessions:</h3>
                <ul class="profile-list" style="display: flex; flex-wrap: wrap; gap: 10px; padding-left: 0; list-style-type: none;">
                    <li style="border: 1px solid var(--border-color); padding: 4px 12px; border-radius: 4px; font-size: 0.95rem; background: white; margin-bottom: 0;">Vibecoding</li>
                    <li style="border: 1px solid var(--border-color); padding: 4px 12px; border-radius: 4px; font-size: 0.95rem; background: white; margin-bottom: 0;">Chess</li>
                    <li style="border: 1px solid var(--border-color); padding: 4px 12px; border-radius: 4px; font-size: 0.95rem; background: white; margin-bottom: 0;">Woodworking</li>
                    <li style="border: 1px solid var(--border-color); padding: 4px 12px; border-radius: 4px; font-size: 0.95rem; background: white; margin-bottom: 0;">Outdoor Cafes</li>
                    <li style="border: 1px solid var(--border-color); padding: 4px 12px; border-radius: 4px; font-size: 0.95rem; background: white; margin-bottom: 0;">Camping <span style="color: var(--text-muted); font-size: 0.85rem;">(mostly eating/chatting by the fire)</span></li>
                    <li style="border: 1px solid var(--border-color); padding: 4px 12px; border-radius: 4px; font-size: 0.95rem; background: white; margin-bottom: 0;">Rock Climbing</li>
                    <li style="border: 1px solid var(--border-color); padding: 4px 12px; border-radius: 4px; font-size: 0.95rem; background: white; margin-bottom: 0;">Dancing</li>
                </ul>
            </div>

        </div>

        <a href="index.html#bio" class="back-link" style="margin-top: 80px; display: inline-block;">← RETURN_TO_BASE</a>
    </div>

    <script>lucide.createIcons();</script>
</body>

</html>
"""

with open("profile.html", "w") as f:
    f.write(html_content)

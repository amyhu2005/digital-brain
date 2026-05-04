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

    <div class="blog-container" style="padding: 140px 2rem 100px 2rem; max-width: 900px; margin: 0 auto; width: 100%;">
        <div class="blog-header" style="margin-bottom: 80px;">
            <p class="blog-subtitle" style="margin-bottom: 20px; line-height: 20px; font-size: 1rem;">// IDENT // CORE_PROFILE</p>
            <h1 class="blog-page-title" style="line-height: 80px; margin-bottom: 20px; font-size: 5rem;">Profile</h1>
        </div>

        <div class="content-body" style="display: flex; flex-direction: column; gap: 80px; line-height: 40px;">

            <!-- Bio Header -->
            <div>
                <h2 style="font-size: 4rem; font-weight: 800; margin-bottom: 20px; letter-spacing: -0.02em; line-height: 60px;">Amy Hu
                </h2>
                <p
                    style="font-family: var(--mono-font); font-size: 1.1rem; color: var(--text-muted); letter-spacing: 0.05em; line-height: 20px; margin-bottom: 20px;">
                    AGE 20 // UCSD CLASS OF 2027</p>
                <p style="margin-top: 0; font-size: 1.5rem; font-weight: 500; line-height: 40px;">Bachelors of Economics and Masters of
                    Public Policy</p>
            </div>

            <!-- Location -->
            <div>
                <h3
                    style="font-family: var(--mono-font); font-size: 1rem; color: var(--accent-orange); text-transform: uppercase; margin-bottom: 20px; letter-spacing: 0.1em; line-height: 20px;">
                    Location</h3>
                <ul style="list-style: none; padding: 0; font-size: 1.25rem;">
                    <li style="margin-bottom: 20px; line-height: 40px;"><strong style="color: var(--text-main);">Currently:</strong>
                        San Diego, CA</li>
                    <li style="margin-bottom: 20px; line-height: 40px;"><strong style="color: var(--text-main);">Summer
                            2026:</strong> Berlin</li>
                    <li style="margin-bottom: 0; line-height: 40px;"><strong style="color: var(--text-main);">Home:</strong>
                        Cupertino, CA</li>
                </ul>
            </div>

            <!-- Hats & Work -->
            <div>
                <h3
                    style="font-family: var(--mono-font); font-size: 1rem; color: var(--accent-orange); text-transform: uppercase; margin-bottom: 20px; letter-spacing: 0.1em; line-height: 20px;">
                    Current Hats</h3>
                <ul style="list-style: none; padding: 0; font-size: 1.25rem;">
                    <li style="margin-bottom: 40px; padding-left: 20px; border-left: 3px solid var(--border-color); line-height: 40px;">
                        <strong style="display: block; margin-bottom: 0;">Research Assistant</strong>
                        <span style="color: var(--text-muted); display: block; font-size: 1.1rem;">Researching Macroeconomic uncertainty shocks</span>
                    </li>
                    <li style="margin-bottom: 40px; padding-left: 20px; border-left: 3px solid var(--border-color); line-height: 40px;">
                        <strong style="display: block; margin-bottom: 0;">Resident Assistant</strong>
                        <span style="color: var(--text-muted); display: block; font-size: 1.1rem;">UCSD 7th College Resident Life</span>
                    </li>
                    <li style="margin-bottom: 20px; padding-left: 20px; border-left: 3px solid var(--border-color); line-height: 40px;">
                        <strong style="display: block; margin-bottom: 0;">Consultant</strong>
                        <span style="color: var(--text-muted); display: block; font-size: 1.1rem;">UCSD Global Policy School Consulting</span>
                    </li>
                </ul>
                <div class="tech-tag orange"
                    style="position: static; margin-top: 40px; border: 1px solid var(--accent-orange); padding: 20px 30px; display: inline-block; background: rgba(255, 77, 0, 0.05); font-size: 1rem; line-height: 40px;">
                    [ STATUS: OPEN TO OPPORTUNITIES ] <br> Seeking opportunities in Berlin (late June–early August
                    2026), with flexibility to work remotely before or after this period.
                </div>
            </div>

            <!-- Chipping away -->
            <div>
                <h3
                    style="font-family: var(--mono-font); font-size: 1rem; color: var(--accent-orange); text-transform: uppercase; margin-bottom: 20px; letter-spacing: 0.1em; line-height: 20px;">
                    Chipping away at</h3>
                <ul style="padding-left: 20px; color: var(--text-main); font-size: 1.25rem;">
                    <li style="margin-bottom: 40px; line-height: 40px;"><em>Linear Algebra and Its Applications (4th edition)</em> <br><span style="color: var(--text-muted); font-size: 1rem; font-family: var(--mono-font); letter-spacing: 0.05em;">[GILBERT STRANG]</span></li>
                    <li style="margin-bottom: 40px; line-height: 40px;"><em>An Introduction to Statistical Reasoning with Application in
                        Python</em> <br><span style="color: var(--text-muted); font-size: 1rem; font-family: var(--mono-font); letter-spacing: 0.05em;">[GARETH JAMES ET AL.]</span></li>
                    <li style="margin-bottom: 0; line-height: 40px;"><em>Glial Neurobiology</em> <br><span style="color: var(--text-muted); font-size: 1rem; font-family: var(--mono-font); letter-spacing: 0.05em;">[ALEXEI VERKHRATSKY, ARTHUR BUTT]</span></li>
                </ul>
            </div>

            <!-- Currently Reading -->
            <div>
                <h3
                    style="font-family: var(--mono-font); font-size: 1rem; color: var(--accent-orange); text-transform: uppercase; margin-bottom: 20px; letter-spacing: 0.1em; line-height: 20px;">
                    Currently Reading</h3>
                <p style="font-size: 1.5rem; line-height: 40px; margin-bottom: 0;"><em>Cat's Cradle</em> <br><span
                        style="color: var(--text-muted); font-size: 1rem; font-family: var(--mono-font); letter-spacing: 0.05em;">[KURT VONNEGUT]</span></p>
            </div>

            <!-- Obsessions -->
            <div>
                <h3
                    style="font-family: var(--mono-font); font-size: 1rem; color: var(--accent-orange); text-transform: uppercase; margin-bottom: 20px; letter-spacing: 0.1em; line-height: 20px;">
                    Current Obsessions</h3>
                <div style="display: flex; flex-wrap: wrap; gap: 15px;">
                    <span
                        style="border: 1px solid var(--border-color); padding: 8px 20px; border-radius: 30px; font-size: 1.1rem; background: white; transition: all 0.3s ease; box-shadow: 2px 2px 0px rgba(0,0,0,0.05); line-height: 24px; height: 40px; display: inline-flex; align-items: center;">Vibecoding</span>
                    <span
                        style="border: 1px solid var(--border-color); padding: 8px 20px; border-radius: 30px; font-size: 1.1rem; background: white; transition: all 0.3s ease; box-shadow: 2px 2px 0px rgba(0,0,0,0.05); line-height: 24px; height: 40px; display: inline-flex; align-items: center;">Chess</span>
                    <span
                        style="border: 1px solid var(--border-color); padding: 8px 20px; border-radius: 30px; font-size: 1.1rem; background: white; transition: all 0.3s ease; box-shadow: 2px 2px 0px rgba(0,0,0,0.05); line-height: 24px; height: 40px; display: inline-flex; align-items: center;">Woodworking</span>
                    <span
                        style="border: 1px solid var(--border-color); padding: 8px 20px; border-radius: 30px; font-size: 1.1rem; background: white; transition: all 0.3s ease; box-shadow: 2px 2px 0px rgba(0,0,0,0.05); line-height: 24px; height: 40px; display: inline-flex; align-items: center;">Outdoor Cafes</span>
                    <span
                        style="border: 1px solid var(--border-color); padding: 8px 20px; border-radius: 30px; font-size: 1.1rem; background: white; transition: all 0.3s ease; box-shadow: 2px 2px 0px rgba(0,0,0,0.05); line-height: 24px; height: 40px; display: inline-flex; align-items: center;">Camping <span style="color: var(--text-muted); font-size: 0.9rem; margin-left: 6px;">(mostly eating/chatting by the fire)</span></span>
                    <span
                        style="border: 1px solid var(--border-color); padding: 8px 20px; border-radius: 30px; font-size: 1.1rem; background: white; transition: all 0.3s ease; box-shadow: 2px 2px 0px rgba(0,0,0,0.05); line-height: 24px; height: 40px; display: inline-flex; align-items: center;">Rock Climbing</span>
                    <span
                        style="border: 1px solid var(--border-color); padding: 8px 20px; border-radius: 30px; font-size: 1.1rem; background: white; transition: all 0.3s ease; box-shadow: 2px 2px 0px rgba(0,0,0,0.05); line-height: 24px; height: 40px; display: inline-flex; align-items: center;">Dancing</span>
                </div>
            </div>

        </div>

        <a href="index.html#bio" class="back-link" style="margin-top: 80px; line-height: 20px;">← RETURN_TO_BASE</a>
    </div>

    <script>lucide.createIcons();</script>
</body>

</html>
"""

with open("profile.html", "w") as f:
    f.write(html_content)

import re
import glob

def convert_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the intro paragraph and insert the color bar right after it
    # The intro paragraph is the first <p> after <div class="content-body">
    intro_match = re.search(r'(<div class="content-body">.*?<p[^>]*>.*?</p>)', content, flags=re.DOTALL)
    
    if intro_match and 'color-palette-bar' not in content:
        color_bar = """
            <div class="color-palette-bar">
                <div class="color-swatch" style="background: #1a1a1a;" data-hex="#1A1A1A"></div>
                <div class="color-swatch" style="background: #333333;" data-hex="#333333"></div>
                <div class="color-swatch" style="background: #666666;" data-hex="#666666"></div>
                <div class="color-swatch" style="background: #d1d1d1;" data-hex="#D1D1D1"></div>
                <div class="color-swatch" style="background: #ff4d00;" data-hex="#FF4D00"></div>
            </div>"""
        
        # Insert color bar
        content = content[:intro_match.end()] + color_bar + content[intro_match.end():]

    # Replace doc modules
    # <div class="doc-module"> ... </div>
    # Using regex to find them.
    pattern = r'<div class="doc-module">\s*<img src="([^"]+)" alt="([^"]+)" class="doc-module-img">\s*<h3 class="doc-module-title">([^<]+)</h3>\s*<p class="doc-module-desc">([^<]+)</p>\s*</div>'
    
    def repl(m):
        img_src = m.group(1)
        img_alt = m.group(2)
        title = m.group(3)
        desc = m.group(4)
        
        return f"""
            <div class="case-study-module">
                <div class="case-image-wrapper">
                    <img src="{img_src}" alt="{img_alt}">
                </div>
                <div class="case-text-wrapper">
                    <div class="tech-tag orange" style="position: static; margin-bottom: 1rem;">// MODULE_FOCUS</div>
                    <h3 class="case-text-title">{title}</h3>
                    <p class="case-text-desc">{desc}</p>
                </div>
            </div>"""
            
    new_content = re.sub(pattern, repl, content)

    if content != new_content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for f in ['logicforge.html', 'proliphia.html', 'aurachess.html', 'timeblocking.html']:
    convert_file(f)

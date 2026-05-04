(function() {
    let isAdmin = false;
    
    // Toggle Admin Mode with Ctrl + Shift + E
    window.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.shiftKey && e.code === 'KeyE') {
            e.preventDefault();
            isAdmin = !isAdmin;
            
            document.body.contentEditable = isAdmin;
            
            // Create/Show save button only when needed
            let saveBtn = document.getElementById('cms-save-btn');
            if (isAdmin) {
                if (!saveBtn) {
                    saveBtn = document.createElement('button');
                    saveBtn.id = 'cms-save-btn';
                    saveBtn.innerText = 'Save Changes';
                    saveBtn.style.cssText = `
                        position: fixed; bottom: 20px; right: 20px; padding: 10px 20px;
                        background: #800000; color: white; border: none; border-radius: 5px;
                        cursor: pointer; z-index: 99999; font-family: inherit; font-size: 0.8rem;
                    `;
                    saveBtn.onclick = savePage;
                    document.body.appendChild(saveBtn);
                }
                saveBtn.style.display = 'block';
                document.body.style.boxShadow = 'inset 0 0 10px rgba(128,0,0,0.5)';
            } else {
                if (saveBtn) saveBtn.style.display = 'none';
                document.body.style.boxShadow = 'none';
            }

            const links = document.querySelectorAll('a');
            links.forEach(l => l.style.pointerEvents = isAdmin ? 'none' : 'auto');
        }
    });

    async function savePage() {
        const saveBtn = document.getElementById('cms-save-btn');
        saveBtn.innerText = 'Saving...';
        
        // 1. TEMPORARILY CLEAN UP FOR THE SAVE
        document.body.contentEditable = 'false';
        document.body.style.boxShadow = 'none';
        saveBtn.remove(); // Remove own button from DOM
        
        // Remove any browser-injected snackbars or glows
        document.querySelectorAll('#accel-snackbar').forEach(el => el.remove());
        
        // Reset splash opacity so it's not saved as hidden
        const splash = document.querySelector('.splash');
        if (splash) splash.style.opacity = '';
        
        // Clean up inline styles that might have been added by the flashlight script
        const existence = document.querySelector('.existence-text');
        if (existence) existence.style.clipPath = '';

        // 2. CAPTURE THE CLEAN HTML
        const cleanHTML = '<!DOCTYPE html>\n' + document.documentElement.outerHTML;

        // 3. SEND TO SERVER
        let filename = window.location.pathname.split('/').pop() || 'index.html';
        try {
            const response = await fetch('/save', {
                method: 'POST',
                body: JSON.stringify({ filename, content: cleanHTML }),
                headers: { 'Content-Type': 'application/json' }
            });
            if (response.ok) alert('Saved successfully!');
            else throw new Error();
        } catch (err) {
            alert('Failed to save. Is cms.py running?');
        }

        // 4. RESTORE UI
        location.reload(); // Reload to get a fresh clean state
    }
})();


document.addEventListener("DOMContentLoaded", function () {
    // =========================
    // HEADER ELEMENTS
    // =========================

    const menuBtn =
        document.getElementById("menuBtn") ||
        document.getElementById("menuButton");

    const sideMenu =
        document.getElementById("sideMenu") ||
        document.getElementById("dashboardSidebar");

    const menuOverlay =
        document.getElementById("menuOverlay") ||
        document.getElementById("sidebarOverlay");

    const themeBtn =
        document.getElementById("themeBtn") ||
        document.getElementById("themeButton");

    // =========================
    // MENU
    // =========================

    function openMenu() {
        if (sideMenu) {
            sideMenu.classList.add("active");
        }

        if (menuOverlay) {
            menuOverlay.classList.add("active");
        }

        if (menuBtn) {
            menuBtn.setAttribute("aria-expanded", "true");
        }

        document.body.classList.add("menu-open");
    }

    function closeMenu() {
        if (sideMenu) {
            sideMenu.classList.remove("active");
        }

        if (menuOverlay) {
            menuOverlay.classList.remove("active");
        }

        if (menuBtn) {
            menuBtn.setAttribute("aria-expanded", "false");
        }

        document.body.classList.remove("menu-open");
    }

    if (menuBtn) {
        menuBtn.setAttribute("aria-expanded", "false");

        menuBtn.addEventListener("click", function (event) {
            event.preventDefault();

            if (sideMenu && sideMenu.classList.contains("active")) {
                closeMenu();
            } else {
                openMenu();
            }
        });
    }

    if (menuOverlay) {
        menuOverlay.addEventListener("click", closeMenu);
    }

    // Close menu when a sidebar link is selected.
    if (sideMenu) {
        sideMenu.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", closeMenu);
        });
    }

    // =========================
    // DARK / LIGHT THEME
    // =========================

    function updateThemeIcon() {
        if (!themeBtn) {
            return;
        }

        const isDark =
            document.body.classList.contains("dark-mode");

        if (isDark) {
            themeBtn.textContent = "🌙";
            themeBtn.setAttribute(
                "aria-label",
                "Switch to light mode"
            );
            themeBtn.setAttribute(
                "title",
                "Switch to light mode"
            );
        } else {
            themeBtn.textContent = "☀️";
            themeBtn.setAttribute(
                "aria-label",
                "Switch to dark mode"
            );
            themeBtn.setAttribute(
                "title",
                "Switch to dark mode"
            );
        }
    }

    try {
        const savedTheme =
            localStorage.getItem("semesterExpressTheme");

        if (savedTheme === "dark") {
            document.body.classList.add("dark-mode");
        } else if (savedTheme === "light") {
            document.body.classList.remove("dark-mode");
        }
    } catch (error) {
        // Theme toggle will still work if storage is unavailable.
    }

    updateThemeIcon();

    if (themeBtn) {
        themeBtn.addEventListener("click", function (event) {
            event.preventDefault();

            document.body.classList.toggle("dark-mode");

            const isDark =
                document.body.classList.contains("dark-mode");

            try {
                localStorage.setItem(
                    "semesterExpressTheme",
                    isDark ? "dark" : "light"
                );
            } catch (error) {
                // The theme works for the current page even
                // if the browser cannot save the preference.
            }

            updateThemeIcon();
        });
    }

    // =========================
    // CLOSE MENU WITH ESCAPE
    // =========================

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeMenu();
        }
    });
});
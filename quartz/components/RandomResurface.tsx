import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

export default (() => {
  function RandomResurface(_props: QuartzComponentProps) {
    return <div id="random-resurface-widget" />
  }

  RandomResurface.afterDOMLoaded = `
    (function() {
      const STORAGE_KEY = "resurface-dismissed";
      const WIDGET_KEY = "resurface-cards";
      const COUNT = 4;

      // Get dismissed slugs from sessionStorage
      function getDismissed() {
        try { return JSON.parse(sessionStorage.getItem(STORAGE_KEY) || "[]"); }
        catch { return []; }
      }
      function addDismissed(slug) {
        const d = getDismissed();
        d.push(slug);
        sessionStorage.setItem(STORAGE_KEY, JSON.stringify(d));
      }

      // Pick N random items from array, excluding dismissed
      function pickRandom(arr, n, excluded) {
        const pool = arr.filter(x => !excluded.includes(x.id));
        const shuffled = pool.sort(() => Math.random() - 0.5);
        return shuffled.slice(0, n);
      }

      async function init() {
        const widget = document.getElementById("random-resurface-widget");
        if (!widget) return;

        // If widget was fully dismissed this session, don't show
        if (sessionStorage.getItem("resurface-hidden") === "1") return;

        // Fetch the Quartz content index
        let nodes = [];
        try {
          const resp = await fetch("/static/contentIndex.json");
          const data = await resp.json();
          // contentIndex is an object keyed by slug
          nodes = Object.entries(data).map(([id, meta]) => ({
            id,
            title: meta.title || id,
            description: meta.description || "",
          })).filter(n => !n.id.startsWith("raw/") && n.id !== "index" && !n.id.endsWith("/index"));
        } catch(e) {
          return; // silently fail if index not available
        }

        const dismissed = getDismissed();
        const cards = pickRandom(nodes, COUNT, dismissed);
        if (cards.length === 0) return;

        widget.innerHTML = \`
          <div class="resurface-container">
            <div class="resurface-header">
              <span class="resurface-title">✨ Resurface</span>
              <button class="resurface-close" title="Hide">✕</button>
            </div>
            <div class="resurface-cards">
              \${cards.map(c => \`
                <a class="resurface-card" href="/\${c.id}" data-slug="\${c.id}">
                  <div class="resurface-card-title">\${c.title}</div>
                  \${c.description ? \`<div class="resurface-card-desc">\${c.description.slice(0, 60)}…</div>\` : ""}
                  <button class="resurface-dismiss" data-slug="\${c.id}" title="Dismiss">✕</button>
                </a>
              \`).join("")}
            </div>
          </div>
        \`;

        // Close entire widget
        widget.querySelector(".resurface-close")?.addEventListener("click", () => {
          sessionStorage.setItem("resurface-hidden", "1");
          widget.innerHTML = "";
        });

        // Dismiss individual cards
        widget.querySelectorAll(".resurface-dismiss").forEach(btn => {
          btn.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            const slug = btn.getAttribute("data-slug");
            addDismissed(slug);
            btn.closest(".resurface-card")?.remove();
            if (widget.querySelectorAll(".resurface-card").length === 0) {
              widget.innerHTML = "";
            }
          });
        });
      }

      // Run after page settles
      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
      } else {
        init();
      }
    })();
  `

  RandomResurface.css = `
    #random-resurface-widget {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      max-width: 280px;
      font-size: 0.8rem;
    }
    .resurface-container {
      background: var(--light);
      border: 1px solid var(--lightgray);
      border-radius: 10px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.18);
      overflow: hidden;
    }
    .resurface-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 12px;
      border-bottom: 1px solid var(--lightgray);
      background: var(--secondary);
    }
    .resurface-title {
      font-weight: 600;
      color: var(--light);
      font-size: 0.75rem;
      letter-spacing: 0.03em;
    }
    .resurface-close {
      background: none;
      border: none;
      cursor: pointer;
      color: var(--light);
      opacity: 0.7;
      font-size: 0.75rem;
      padding: 0;
      line-height: 1;
    }
    .resurface-close:hover { opacity: 1; }
    .resurface-cards {
      display: flex;
      flex-direction: column;
    }
    .resurface-card {
      display: block;
      position: relative;
      padding: 8px 32px 8px 12px;
      text-decoration: none;
      color: var(--dark);
      border-bottom: 1px solid var(--lightgray);
      transition: background 0.12s;
    }
    .resurface-card:last-child { border-bottom: none; }
    .resurface-card:hover { background: var(--lightgray); }
    .resurface-card-title {
      font-weight: 500;
      font-size: 0.78rem;
      line-height: 1.3;
    }
    .resurface-card-desc {
      font-size: 0.68rem;
      color: var(--gray);
      margin-top: 2px;
    }
    .resurface-dismiss {
      position: absolute;
      top: 50%;
      right: 8px;
      transform: translateY(-50%);
      background: none;
      border: none;
      cursor: pointer;
      color: var(--gray);
      font-size: 0.65rem;
      opacity: 0;
      transition: opacity 0.12s;
      padding: 2px 4px;
    }
    .resurface-card:hover .resurface-dismiss { opacity: 1; }
    .resurface-dismiss:hover { color: var(--dark); }

    @media (max-width: 768px) {
      #random-resurface-widget { display: none; }
    }
  `

  return RandomResurface
}) satisfies QuartzComponentConstructor

document$.subscribe(() => {

  function prepareMermaidSources() {
    document.querySelectorAll(".mermaid").forEach(el => {
      if (!el.dataset.source) {
        el.dataset.source = el.textContent;
      }
    });
  }

  async function renderMermaid() {

    const isDark =
      document.body.getAttribute("data-md-color-scheme") === "slate";

    mermaid.initialize({
      startOnLoad: false,
      theme: isDark ? "dark" : "default"
    });

    document.querySelectorAll(".mermaid").forEach(el => {
      el.innerHTML = el.dataset.source;
      el.removeAttribute("data-processed");
    });

    await mermaid.run({
      querySelector: ".mermaid"
    });
  }

  prepareMermaidSources();
  renderMermaid();

  const observer = new MutationObserver(() => {
    renderMermaid();
  });

  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"]
  });

});
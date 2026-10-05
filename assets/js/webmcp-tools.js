/* webmcp-tools.js — imperative WebMCP tool registration for shanklin.ai.
 *
 * WebMCP is a proposed W3C standard (Web Machine Learning Community Group)
 * that lets pages expose structured tools to browser-based AI agents.
 * This file is progressive enhancement: on browsers without WebMCP support
 * it does nothing and never throws.
 */
(function () {
  'use strict';
  try {
    var nav = (typeof navigator !== 'undefined') ? navigator : {};
    var doc = (typeof document !== 'undefined') ? document : {};
    var mc = nav.modelContext || doc.modelContext;
    if (!mc || typeof mc.registerTool !== 'function') return;

    // Mirror the site's existing theme mechanism exactly:
    // documentElement[data-theme] + localStorage['reeves-theme'] + button state.
    function setTheme(t) {
      if (t !== 'light' && t !== 'dark' && t !== 'ai') return;
      document.documentElement.setAttribute('data-theme', t);
      try { localStorage.setItem('reeves-theme', t); } catch (e) {}
      var btns = document.querySelectorAll('[data-set-theme]');
      for (var i = 0; i < btns.length; i++) {
        var b = btns[i];
        if (b.classList && typeof b.classList.toggle === 'function') {
          b.classList.toggle('on', b.getAttribute('data-set-theme') === t);
        }
      }
    }

    mc.registerTool({
      name: 'setTheme',
      description: 'Switch the shanklin.ai site theme: light, dark, or ai (the ai theme is a plain machine-readable black-on-white view)',
      inputSchema: {
        type: 'object',
        properties: {
          theme: { type: 'string', enum: ['light', 'dark', 'ai'] }
        },
        required: ['theme'],
        additionalProperties: false
      },
      execute: function (args) {
        try {
          var theme = args && args.theme;
          setTheme(theme);
          return { ok: true, theme: theme };
        } catch (e) {
          return { ok: false, error: 'theme switch failed' };
        }
      }
    });
  } catch (e) {
    /* WebMCP unavailable or registration failed — stay silent. */
  }
})();

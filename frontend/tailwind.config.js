module.exports = {
  presets: [require('frappe-ui/src/utils/tailwind.config')],
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'health-purple': '#453D89',
        'health-pink': '#C8499A',
        'health-ink': '#302B3A',
        'health-deep': '#27233B',
        'health-muted': '#756F82',
        'health-border': '#EAE6F0',
        'health-bg': '#FAF8FC',
      },
      backgroundImage: {
        'health-gradient':
          'linear-gradient(90deg, #453D89, #C8499A)',
        'health-gradient-soft':
          'linear-gradient(90deg, rgba(69, 61, 137, 0.10), rgba(200, 73, 154, 0.08))',
      },
      boxShadow: {
        'health-card':
          '0 10px 34px rgba(39, 35, 59, 0.07), 0 2px 6px rgba(39, 35, 59, 0.04)',
        'health-panel': '0 28px 70px rgba(39, 35, 59, 0.18)',
      },
    },
  },
  plugins: [],
}

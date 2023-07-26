/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./blog/{static,templates}/**/*.{html,js}"],
  theme: {
    fontFamily: {
      'sans': ['Roboto', 'arial'],
      'serif': ['"Roboto Slab"', '"Times New Roman"'],
      'mono': ['"Roboto Mono"', "monospace"],
      'display': ['Inter', 'Roboto', 'Arial']
    },
    transitionProperty: {
      'all': 'all',
      'size': 'width, height, padding, margin',
      'position': 'top, left, right, bottom, transform',
      'movinglabel': 'top, left, right, bottom font-size, font-weight',
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

module.exports = {
  mode: "jit",
  purge: [
    "app/templates/app/*.html",
    "accounts/templates/accounts/*.html", 
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};

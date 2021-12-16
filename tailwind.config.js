module.exports = {
  mode: "jit",
  content: [
    "app/templates/app/*.html",
    "accounts/templates/accounts/*.html",
    "templates/registration/*.html",
    "templates/*.html",
    "tailwind/misc/*.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

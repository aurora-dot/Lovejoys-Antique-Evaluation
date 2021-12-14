module.exports = {
  mode: "jit",
  content: [
    "app/templates/app/*.html",
    "accounts/templates/accounts/*.html",
    "templates/registration/*.html",
    "templates/*.html",
    "form_tailwind/*.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

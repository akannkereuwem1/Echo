 /** @type {import('tailwindcss').Config} */
module.exports = {
  // Look in the static src files and Flask templates for class names
  // Only scan these project-relative paths to avoid scanning outside the repo
  content: [
   
    "../templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

// This is a minimal config.
// If you need the full config, get it from here:
// https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
module.exports = {
    purge: [
      // Templates within theme app (e.g. base.html)
    '../templates/**/*.html',
    // Templates in other apps
    '../../templates/**/*.html',
    // Ignore files in node_modules 
    '!../../**/node_modules',
    // Include JavaScript files that might contain Tailwind CSS classes      
    '../../**/*.js',
    // Include Python files that might contain Tailwind CSS classes
    '../../**/*.py'      
  ],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {},
    },
    variants: {
        extend: {
            borderWidth: ['responsive', 'hover', 'focus'],
            animation: ['responsive', 'motion-safe', 'motion-reduce'],
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
        require('@tailwindcss/forms'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}

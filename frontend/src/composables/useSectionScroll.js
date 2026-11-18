export function useSectionScroll() {
  function scrollToSection(id) {
    const section = document.getElementById(id)
    if (!section) return

    section.scrollIntoView({
      behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches
        ? 'auto'
        : 'smooth',
      block: 'start',
    })
  }

  return { scrollToSection }
}

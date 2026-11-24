<script setup>
import { computed } from 'vue'
import { useLoginUrl } from '@/composables/useLoginUrl'
import { useSectionScroll } from '@/composables/useSectionScroll'

const { loginUrl } = useLoginUrl()
const { scrollToSection } = useSectionScroll()
const year = computed(() => new Date().getFullYear())

const qbLogo = '/files/quantumberg-logo.png'

const links = [
  { label: 'Home', target: 'home' },
  { label: 'Features', target: 'features' },
  { label: 'Benefits', target: 'benefits' },
]

function onNavClick(event, target) {
  event.preventDefault()
  scrollToSection(target)
}
</script>

<template>
  <footer class="bg-[#301044] text-white">
    <div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
      <div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-[1.4fr_0.8fr_0.8fr_1.5fr]">
        <div>
          <img :src="qbLogo" alt="QB Logo" class="h-8 w-auto lg:h-9">
          <p class="mt-4 max-w-md text-sm leading-7 text-white/65">
            A connected healthcare workspace for patient care, hospital
            operations, billing, pharmacy, finance, and reporting.
          </p>
        </div>

        <nav aria-label="Footer">
          <h2 class="text-xs font-bold uppercase tracking-[0.16em] text-white/45">
            Explore
          </h2>
          <ul class="mt-4 space-y-2.5">
            <li v-for="link in links" :key="link.target">
              <a :href="`#${link.target}`"
                class="rounded text-sm text-white/75 transition-colors hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/60"
                @click="onNavClick($event, link.target)">
                {{ link.label }}
              </a>
            </li>
          </ul>
        </nav>

        <nav aria-label="Resources">
          <h2 class="text-xs font-bold uppercase tracking-[0.16em] text-white/45">
            Get started
          </h2>
          <ul class="mt-4 space-y-2.5">
            <li>
              <a :href="loginUrl" class="text-sm text-white/75 transition-colors hover:text-white">
                Open Demo App
              </a>
            </li>
            <li>
              <a href="https://www.quantumberg.com/Contact"
                class="text-sm text-white/75 transition-colors hover:text-white">
                Request a Demo
              </a>
            </li>
          </ul>
        </nav>

        <div>
          <h2 class="text-xs font-bold uppercase tracking-[0.16em] text-white/45">
            Contact
          </h2>
          <ul class="mt-4 space-y-2.5 text-sm text-white/75">
            <li>
              <a href="tel:+919741408044" class="transition-colors hover:text-white">
                +91 97414 08044
              </a>
            </li>
            <li>
              <a href="mailto:admin@quantumberg.com" class="transition-colors hover:text-white">
                admin@quantumberg.com
              </a>
            </li>
            <li>
              <a
                href="https://maps.app.goo.gl/hQjzBozyjy32EtWt7"
                target="_blank"
                rel="noopener noreferrer"
                class="inline-block leading-6 transition-colors hover:text-white"
              >
                No.1376, 2nd floor, 13th Cross, Sarakki Main Rd, 1st Phase, J. P. Nagar, Bengaluru, Karnataka 560078
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="mt-8 border-t border-white/10 pt-5">
        <p class="text-center text-xs text-white/50 sm:text-left">
          &copy; {{ year }} Quantumberg Technologies Pvt Ltd &middot; Healthcare Management System
        </p>
      </div>
    </div>
  </footer>
</template>

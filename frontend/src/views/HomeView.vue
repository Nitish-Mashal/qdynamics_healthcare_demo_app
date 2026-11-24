<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import Navbar from '@/components/layout/Navbar.vue'
import Footer from '@/components/layout/Footer.vue'
import HeroSection from '@/components/landing/HeroSection.vue'
import FeaturesSection from '@/components/landing/FeaturesSection.vue'
import BenefitsSection from '@/components/landing/BenefitsSection.vue'
import CallToAction from '@/components/landing/CallToAction.vue'
import { useSectionScroll } from '@/composables/useSectionScroll'

const whatsappLogo = '/files/whatsapp.png'
const showBackToTop = ref(false)
const { scrollToSection } = useSectionScroll()

function updateScrollButton() {
  showBackToTop.value = window.scrollY > 300
}

onMounted(() => {
  updateScrollButton()
  window.addEventListener('scroll', updateScrollButton, { passive: true })
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', updateScrollButton)
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <Navbar />
    <main>
      <HeroSection />
      <FeaturesSection />
      <BenefitsSection />
      <CallToAction />
    </main>
    <Footer />
    <a
      href="https://wa.me/919741408044"
      target="_blank"
      rel="noopener noreferrer"
      aria-label="Contact Quantumberg on WhatsApp"
      class="fixed bottom-20 right-5 z-40 inline-flex h-10 w-10 items-center justify-center rounded-full bg-[#25D366] shadow-lg transition-transform hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#25D366] focus-visible:ring-offset-2"
    >
      <img :src="whatsappLogo" alt="" class="h-8 w-8 object-contain">
    </a>
    <button
      v-if="showBackToTop"
      type="button"
      aria-label="Back to top"
      class="fixed bottom-5 right-5 z-40 inline-flex h-10 w-10 items-center justify-center rounded-full bg-health-purple text-white shadow-lg transition-transform hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-health-purple focus-visible:ring-offset-2"
      @click="scrollToSection('home')"
    >
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
        stroke-linejoin="round" class="h-6 w-6" aria-hidden="true">
        <path d="M12 19V5M5 12l7-7 7 7" />
      </svg>
    </button>
  </div>
</template>

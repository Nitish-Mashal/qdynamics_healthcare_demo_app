<script setup>
import Navbar from '@/components/layout/Navbar.vue'
import Footer from '@/components/layout/Footer.vue'
import HeroSection from '@/components/landing/HeroSection.vue'
import FeaturesSection from '@/components/landing/FeaturesSection.vue'
import RolesSection from '@/components/landing/RolesSection.vue'
import WorkflowSection from '@/components/landing/WorkflowSection.vue'
import CallToAction from '@/components/landing/CallToAction.vue'
</script>

<template>
  <div class="min-h-screen bg-white">
    <Navbar />
    <main>
      <HeroSection />
      <FeaturesSection />
      <RolesSection />
      <WorkflowSection />
      <CallToAction />
    </main>
    <Footer />
  </div>
</template>

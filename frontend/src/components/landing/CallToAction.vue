<script setup>
import { useLoginUrl } from '@/composables/useLoginUrl'

const { loginUrl } = useLoginUrl()
</script>

<template>
  <section id="contact" class="relative scroll-mt-24 overflow-hidden bg-health-gradient py-20 lg:py-24">
    <div class="pointer-events-none absolute inset-0 opacity-[0.12]" aria-hidden="true"
      style="background-image: radial-gradient(circle at 20% 20%, #fff 1px, transparent 1px); background-size: 22px 22px;" />
    <div class="relative mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
      <p class="text-sm font-bold uppercase tracking-[0.18em] text-pink-200">
        See the system in action
      </p>
      <h2 class="mt-3 text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
        Bring healthcare operations together
      </h2>
      <p class="mx-auto mt-4 max-w-2xl text-lg leading-8 text-white/75">
        Explore how connected patient, clinical, financial, and administrative
        workflows can support your healthcare organization.
      </p>
      <div class="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
        <a :href="loginUrl"
          class="inline-flex w-full items-center justify-center gap-2 rounded-xl bg-white px-6 py-2.5 font-semibold text-health-deep shadow-lg transition-transform hover:-translate-y-0.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-health-deep sm:w-auto">
          Open Demo App
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
            stroke-linejoin="round" class="h-4 w-4" aria-hidden="true">
            <path d="M5 12h14M13 6l6 6-6 6" />
          </svg>
        </a>
        <a href="https://www.quantumberg.com/Contact"
          class="inline-flex w-full items-center justify-center rounded-xl border-2 border-white/60 px-6 py-2.5 font-semibold text-white transition-colors hover:bg-white/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white sm:w-auto">
          Request a Demo
        </a>
      </div>
    </div>
  </section>
</template>

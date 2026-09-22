<script setup lang="ts">
import { ref } from 'vue'

defineProps<{
  steps: { title: string; body: string }[]
}>()

const open = ref<Record<number, boolean>>({})

function toggle(i: number) {
  open.value = { ...open.value, [i]: !open.value[i] }
}
</script>

<template>
  <div class="ix-steps">
    <div v-for="(step, i) in steps" :key="i" class="ix-step" :class="{ 'is-open': open[i] }">
      <button type="button" class="ix-step__head" :aria-expanded="!!open[i]" @click="toggle(i)">
        <span class="ix-step__num">{{ i + 1 }}</span>
        {{ step.title }}
      </button>
      <div v-show="open[i]" class="ix-step__body">
        <p>{{ step.body }}</p>
      </div>
    </div>
  </div>
</template>

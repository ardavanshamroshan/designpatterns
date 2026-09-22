<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  question: string
  options: string[]
  answer: number
  ok?: string
  no?: string
}>()

const done = ref(false)
const picked = ref<number | null>(null)

function choose(i: number) {
  if (done.value) return
  done.value = true
  picked.value = i
}
</script>

<template>
  <div class="ix-quiz">
    <p class="ix-quiz__q">{{ question }}</p>
    <div class="ix-quiz__opts">
      <button
        v-for="(opt, i) in options"
        :key="i"
        type="button"
        class="ix-quiz__opt"
        :class="{
          'is-correct': done && i === answer,
          'is-wrong': done && picked === i && i !== answer,
        }"
        :disabled="done"
        @click="choose(i)"
      >
        {{ opt }}
      </button>
    </div>
    <p
      v-if="done"
      class="ix-quiz__fb"
      :class="picked === answer ? 'is-ok' : 'is-no'"
    >
      {{ picked === answer ? ok || 'Correct.' : no || 'Not quite.' }}
    </p>
  </div>
</template>

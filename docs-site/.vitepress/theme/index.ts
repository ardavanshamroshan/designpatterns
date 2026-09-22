import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import Layout from './Layout.vue'
import CompareCode from './components/CompareCode.vue'
import Quiz from './components/Quiz.vue'
import StepsReveal from './components/StepsReveal.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    app.component('CompareCode', CompareCode)
    app.component('Quiz', Quiz)
    app.component('StepsReveal', StepsReveal)
  },
} satisfies Theme

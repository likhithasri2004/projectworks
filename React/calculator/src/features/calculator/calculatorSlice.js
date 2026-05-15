import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  value: '',
}

const calculatorSlice = createSlice({
  name: 'calculator',
  initialState,
  reducers: {
    addValue: (state, action) => {
      state.value += action.payload
    },

    clearValue: (state) => {
      state.value = ''
    },

    // ✅ NEW: delete one digit
    deleteLast: (state) => {
      state.value = state.value.slice(0, -1)
    },

    calculateResult: (state) => {
      try {
        state.value = eval(state.value).toString()
      } catch {
        state.value = 'Error'
      }
    },
  },
})

export const {
  addValue,
  clearValue,
  deleteLast,        // ✅ export this
  calculateResult,
} = calculatorSlice.actions

export default calculatorSlice.reducer
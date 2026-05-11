import { useDispatch, useSelector } from 'react-redux'
import {
  addValue,
  clearValue,
  calculateResult,
} from '../../features/calculator/calculatorSlice'
import './Calculator.css'

export default function Calculator() {
  const dispatch = useDispatch()
  const value = useSelector((state) => state.calculator.value)

  const buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+',
  ]

  return (
    <div className="calculator">
      <input type="text" value={value} readOnly />

      <div className="buttons">
        {buttons.map((btn) =>
          btn === '=' ? (
            <button key={btn} onClick={() => dispatch(calculateResult())}>
              =
            </button>
          ) : (
            <button
              key={btn}
              onClick={() => dispatch(addValue(btn))}
            >
              {btn}
            </button>
          )
        )}
        <button className="clear" onClick={() => dispatch(clearValue())}>
          C
        </button>
      </div>
    </div>
  )
}
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

        {/* ⌫ Backspace */}
        <button
          className="operator"
          onClick={() => dispatch(deleteLast())}
        >
          ⌫
        </button>

        {/* Clear */}
        <button
          className="clear"
          onClick={() => dispatch(clearValue())}
        >
          C
        </button>

        {/* Numbers & operators */}
        {buttons.map((btn) =>
          btn === '=' ? (
            <button
              key={btn}
              className="equal"
              onClick={() => dispatch(calculateResult())}
            >
              =
            </button>
          ) : (
            <button
              key={btn}
              className={isNaN(btn) ? 'operator' : ''}
              onClick={() => dispatch(addValue(btn))}
            >
              {btn}
            </button>
          )
        )}
      </div>
    </div>
  )
}
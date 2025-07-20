/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

def main() {
    const n = float(input());
    print(exercise(n));
}

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/

def exercise(n) {
    status = "ALERT" if r > 1.5 else "OK"
    return f"{r}°C — {status}"
}

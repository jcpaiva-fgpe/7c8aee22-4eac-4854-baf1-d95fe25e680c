/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

function main() {
    writeln(exercise());
}

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/

function exercise() {
	global_rise = 1.2
    local_rise = 0.9
    diff = global_rise - local_rise
    print("Difference:", diff, "°C")
}

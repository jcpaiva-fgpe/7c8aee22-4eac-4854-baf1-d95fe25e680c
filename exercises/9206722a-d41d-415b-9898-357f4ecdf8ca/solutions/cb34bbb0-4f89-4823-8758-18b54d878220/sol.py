/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

def main() {
    print(exercise());
}

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/

def exercise() {
	cities = ["Berlin", "Rome", "Madrid"]
    warming = (0.9, 1.3, 1.7)
    city_data = {"Berlin": 0.9, "Rome": 1.3, "Madrid": 1.7}
    return cities + warming + city_data
}

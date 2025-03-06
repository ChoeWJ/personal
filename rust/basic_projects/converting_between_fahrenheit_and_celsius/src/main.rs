// 입력 처리를 위한 std::io 가져오기
use std::io;

// 화씨 절대 영도 값
const FAHRENHEIT_ABSOLUTE_ZERO: f64 = -459.67;

// 섭씨 절대 영도 값
const CELSIUS_ABSOLUTE_ZERO: f64 = -273.15;

// main 함수
fn main() {
    // 입력 유도
    println!("화씨를 입력하면 섭씨로 섭씨를 입력하면 화씨로 변환됩니다");

    // 변환할 온도 타입 설정
    println!("변환할 온도 타입을 입력해주세요. 1.화씨 2.섭씨");
    let mut selection = String::new();
    
    io::stdin().read_line(&mut selection).expect("Falied to read line");

    let selection: i64 = selection.trim().parse().expect("Falied to read line");

    // 온도 값 설정
    println!("변환할 온도 값을 입력해주세요.");
    let mut value = String::new();

    io::stdin().read_line(&mut value).expect("Falied to read line");

    let value: f64 = value.trim().parse().expect("Falied to read line");

    // 변환 타입에 맞는 함수로 온도 값을 전달
    if selection == 1 {
        fahrenheit_to_celsius(value);
    } else {
        celsius_to_fahrenheit(value);
    }
}

// 화씨에서 섭씨로 바꾸는 함수
fn fahrenheit_to_celsius(value: f64) {
    // 섭씨 값 초기화
    let mut celsius = 0.0;
    
    // 화씨 절대 영도 값 판별
    if value <= FAHRENHEIT_ABSOLUTE_ZERO {
        println!("절대 영도보다 낮은 값은 변환할 수 없습니다. 다시 값을 입력해 주세요!");
    } else {
        celsius += (value - 32.0) * (5.0 / 9.0);
        println!("화씨 {}℉ 는 섭씨 {}℃ 입니다", value, celsius);
    }
}

// 섭씨에서 화씨로 바꾸는 함수
fn celsius_to_fahrenheit(value: f64) {
    let mut fahrenheit = 0.0;
    
    // 섭씨 절대 영도 값 판별
    if value <= CELSIUS_ABSOLUTE_ZERO {
        println!("절대 영도보다 낮은 값은 변환할 수 없습니다. 다시 값을 입력해 주세요!");
    } else {
        fahrenheit += (value * (9.0 / 5.0)) + 32.0;
        println!("섭씨 {}℃ 는 화씨 {}℉ 입니다", value, fahrenheit);
    }
}
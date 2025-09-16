plugins {
    application
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter:5.7.2")
    implementation("com.google.guava:guava:30.1.1-jre")
}

application {
    mainClass.set("experimentos.App")
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}

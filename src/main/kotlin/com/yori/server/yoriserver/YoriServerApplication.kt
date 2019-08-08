package com.yori.server.yoriserver

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class YoriServerApplication

fun main(args: Array<String>) {
	runApplication<YoriServerApplication>(*args)
}

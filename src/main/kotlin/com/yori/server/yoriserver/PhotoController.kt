package com.yori.server.yoriserver

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController
class PhotoController {
    @GetMapping("photo")
    fun hello(): String = "Hello World"
}

package com.yori.server.yoriserver

import io.swagger.annotations.ApiOperation
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController
class PhotoController {

    @GetMapping("photo")
    @ApiOperation(value = "Hello Endpoint", notes = "Hello, name!")
    fun hello(): String = "Hello World"
}

package com.yori.server.yoriserver.controller

import io.swagger.annotations.ApiOperation
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

import com.yori.server.yoriserver.Photo

@RestController
class PhotoController {

    @GetMapping("photo")
    @ApiOperation(value = "photo Endpoint", notes = "photo related api")
    fun hello(): Photo {

    return Photo("groupA","memberA","costume","yori",1,"all");
}
}

package com.hua.note.web.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
	
	@RequestMapping("")
	public String index() {
		return "Welcome to my website!";
	}
}

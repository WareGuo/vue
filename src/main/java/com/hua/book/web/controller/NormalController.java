package com.hua.book.web.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NormalController {
	
	@RequestMapping("")
	public String index() {
		return "lcx welcome!";
	}
	
}

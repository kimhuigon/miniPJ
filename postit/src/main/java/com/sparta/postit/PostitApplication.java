package com.sparta.postit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@EnableJpaAuditing
@SpringBootApplication
public class PostitApplication {

	public static void main(String[] args) {
		SpringApplication.run(PostitApplication.class, args);
	}

}

package com.sparta.postit.dto;

import com.sparta.postit.domain.Posts;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class PostsResponseDto {
    private Long id;
    private String title;
    private String content;
    private String author;
    private String pw;

    public PostsResponseDto(Posts entity) {
        this.id = entity.getId();
        this.title = entity.getTitle();
        this.content = entity.getContent();
        this.author = entity.getAuthor();
        this.pw = entity.getPw();
    }
}

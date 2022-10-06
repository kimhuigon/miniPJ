package com.sparta.postit.dto;

import com.sparta.postit.domain.Posts;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class PostsSaveRequestDto {
    private String title;
    private String content;
    private String author;
    private String pw;

    @Builder
    public PostsSaveRequestDto(String title, String content, String author, String pw) {
        this.title = title;
        this.content = content;
        this.author = author;
        this.pw = pw;

    }

    public Posts toEntity() {
        return Posts.builder()
                .title(title)
                .content(content)
                .author(author)
                .pw(pw)
                .build();
    }
}

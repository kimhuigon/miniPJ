package com.sparta.postit.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class PostsUpdateRequestDto {
    private String title;
    private String content;
    private String pw;

    @Builder
    public PostsUpdateRequestDto(String title, String content, String pw) {
        this.title = title;
        this.content = content;
        this.pw = pw;
    }
}

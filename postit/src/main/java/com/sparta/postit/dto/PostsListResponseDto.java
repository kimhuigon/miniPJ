package com.sparta.postit.dto;

import com.sparta.postit.domain.Posts;
import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;

@Getter
@Builder
public class PostsListResponseDto {

    private Long id;
    private String title;
    private String author;
    private String pw;
    private LocalDateTime modifiedDate;

    private LocalDateTime createdDate;

//    public PostsListResponseDto(Posts entity) {
//        this.id = entity.getId();
//        this.title = entity.getTitle();
//        this.author = entity.getAuthor();
//        this.modifiedDate = entity.getModifiedDate();
//    }
}
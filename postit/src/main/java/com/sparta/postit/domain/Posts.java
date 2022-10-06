package com.sparta.postit.domain;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Getter
@NoArgsConstructor
@Entity
public class Posts extends BaseTimeEntity{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(length = 500, nullable = false)
    private String title;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String content;

    private String author;

    private String pw;

    @Builder
    public Posts(String title, String content, String author, String pw) {
        this.title = title;
        this.content = content;
        this.author = author;
        this.pw = pw;
    }

    public void update(String title, String content, String pw) {
        this.title = title;
        this.content = content;
        this.pw = pw;
    }
}

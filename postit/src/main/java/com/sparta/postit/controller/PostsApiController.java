package com.sparta.postit.controller;

import com.sparta.postit.dto.PostsListResponseDto;
import com.sparta.postit.dto.PostsResponseDto;
import com.sparta.postit.dto.PostsSaveRequestDto;
import com.sparta.postit.dto.PostsUpdateRequestDto;
import com.sparta.postit.service.PostsService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class PostsApiController {

    private final PostsService postsService;

    @GetMapping("/api/v1/posts")
    public List<PostsListResponseDto> getPosts() {
        List<PostsListResponseDto> allPosts = postsService.findAllDesc();
        return allPosts;
    }

    @PostMapping("/api/posts/{id}")
    public boolean comparePassword(@PathVariable Long id, @RequestBody PostsResponseDto postPasswordDto) {
        return postsService.comparePassword(id, postPasswordDto);
    }

    @PostMapping("/api/v1/posts")
    public long save(@RequestBody PostsSaveRequestDto requestDto) {
        return postsService.save(requestDto);
    }

    @PutMapping("/api/v1/posts/{id}")
    public long update(@PathVariable Long id, @RequestBody PostsUpdateRequestDto requestDto) {
        return postsService.update(id, requestDto);
    }

    @GetMapping("/api/v1/posts/{id}")
    public PostsResponseDto findById (@PathVariable Long id) {
        return postsService.findById(id);
    }

    @DeleteMapping("/api/v1/posts/{id}")
    public long delete(@PathVariable long id) {
        postsService.delete(id);
        return id;
    }
}

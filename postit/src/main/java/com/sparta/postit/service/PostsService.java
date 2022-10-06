package com.sparta.postit.service;

import com.sparta.postit.domain.Posts;
import com.sparta.postit.dto.PostsListResponseDto;
import com.sparta.postit.dto.PostsResponseDto;
import com.sparta.postit.dto.PostsSaveRequestDto;
import com.sparta.postit.dto.PostsUpdateRequestDto;
import com.sparta.postit.repository.PostsRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

@RequiredArgsConstructor
@Service
public class PostsService {
    private final PostsRepository postsRepository;

    @Transactional
    public long save(PostsSaveRequestDto requestDto) {
        return postsRepository.save(requestDto.toEntity()).getId();
    }

    @Transactional
    public Long update(Long id, PostsUpdateRequestDto requestDto) {
        Posts posts = postsRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("해당 게시글이 없습니다. id= " + id));
                posts.update(requestDto.getTitle(), requestDto.getContent(), requestDto.getPw());
        return id;
    }

    public PostsResponseDto findById (Long id) {
        Posts entity = postsRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("해당 게시글이 없습니다. id= "+ id));

        return new PostsResponseDto(entity);
    }

    @Transactional
    public  void delete(Long id) {
        Posts posts = postsRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("해당 사용자가 없습니다. id="+id));

        postsRepository.delete(posts);

    }

    //전체목록 (title,author,creat,modifide)만 보여주는 로직 (builder사용) ->responseDto에 @Builder를 추가
    @Transactional(readOnly = true)
    public List<PostsListResponseDto> findAllDesc() {
        List<Posts> allPosts = postsRepository.findAllDesc();
        List<PostsListResponseDto> resultList = new ArrayList<>();

        for (Posts posts : allPosts) {
            PostsListResponseDto dto = PostsListResponseDto.builder()
                    .id(posts.getId())
                    .title(posts.getTitle())
                    .author(posts.getAuthor())
                    .pw(posts.getPw())
                    .createdDate(posts.getCreatedDate())
                    .modifiedDate(posts.getModifiedDate())
                    .build();

            resultList.add(dto);
        }
        return resultList;
    }

//    @Transactional(readOnly = true)
//    public List<PostsListResponseDto> findAllDesc() {
//        return postsRepository.findAllDesc().stream()
//                .map(PostsListResponseDto::new)
//                .collect(Collectors.toList());
//    }

    public boolean comparePassword (Long id, PostsResponseDto postPasswordDto) {
        Posts post = postsRepository.findById(id).orElseThrow(
                () -> new NullPointerException("해당 아이디가 존재하지 않습니다."));
        if (Objects.equals(postPasswordDto.getPw(), post.getPw())) {
            return true;
        } else {
            return false;
        }
    }

}

import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { GithubJobService } from './github-job.service';
import { CreateGithubJobDto } from './dto/create-github-job.dto';
import { UpdateGithubJobDto } from './dto/update-github-job.dto';

@Controller('github-job')
export class GithubJobController {
  constructor(private readonly githubJobService: GithubJobService) {}

  @Post()
  create(@Body() createGithubJobDto: CreateGithubJobDto) {
    return this.githubJobService.create(createGithubJobDto);
  }

  @Get()
  findAll() {
    return this.githubJobService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.githubJobService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateGithubJobDto: UpdateGithubJobDto) {
    return this.githubJobService.update(+id, updateGithubJobDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.githubJobService.remove(+id);
  }
}

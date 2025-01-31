import { Injectable, Logger } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';
import { Octokit } from '@octokit/rest';
import { ConfigService } from '@nestjs/config';
import { CreateGithubJobDto } from './dto/create-github-job.dto';
import { UpdateGithubJobDto } from './dto/update-github-job.dto';

@Injectable()
export class GithubJobService {
  constructor(private configService: ConfigService) {}

  private readonly logger = new Logger(GithubJobService.name);
  private octokit = new Octokit({
    auth: this.configService.get('GITHUB_AUTH'),
  });

  // TODO: schedule job to pull once, then job for checking for changes
  // @Cron('45 * * * * *')
  async getUserRepos() {
    try {
      if (this.octokit) {
        const response = await this.octokit.request('GET /users/{username}/repos', {
          username: 'KwesiLarbi',
          headers: {
            "x-github-api-version": "2022-11-28",
          },
        });
        this.logger.log(response);
      }
      this.logger.log("AUTH didn't work");
    } catch (error) {
      this.logger.error(`Error grabbing repo data! ${JSON.stringify(error.response)}`);
    }
  }

  create(createGithubJobDto: CreateGithubJobDto) {
    return 'This action adds a new githubJob';
  }

  findAll() {
    return `This action returns all githubJob`;
  }

  findOne(id: number) {
    return `This action returns a #${id} githubJob`;
  }

  update(id: number, updateGithubJobDto: UpdateGithubJobDto) {
    return `This action updates a #${id} githubJob`;
  }

  remove(id: number) {
    return `This action removes a #${id} githubJob`;
  }
}

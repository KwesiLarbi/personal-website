import { Injectable, Logger } from '@nestjs/common';
import { Cron, CronExpression } from '@nestjs/schedule';
import { Octokit } from '@octokit/rest';
import { ConfigService } from '@nestjs/config';
import { CreateGithubJobDto } from './dto/create-github-job.dto';
import { UpdateGithubJobDto } from './dto/update-github-job.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { GithubRepo } from './entities/github-job.entity';
import { Repository } from 'typeorm';

@Injectable()
export class GithubJobService {
  private octokit;
  private readonly logger;

  constructor(
    @InjectRepository(GithubRepo)
    private repo: Repository<GithubRepo>,
    private configService: ConfigService
  ) {
    this.octokit = new Octokit({
      auth: this.configService.get('GITHUB_AUTH'),
    });

    this.logger = new Logger(GithubJobService.name);
  }

  // TODO: Schedule job to pull once, then job for checking for changes
  // TODO: Check if DB is empty for initial insert
  @Cron(CronExpression.EVERY_10_SECONDS)
  async initialGithubRepoCronJob() {
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

      let count = await this.repo.count()
      if (count === 0) {
        this.logger.log(`Count: ${count}`);
      }

      this.logger.log(`Count: ${count}`)
    } catch (error) {
      this.logger.error(`Error grabbing repo data! ${JSON.stringify(error.response)}`);
    }
  }

  @Cron(CronExpression.EVERY_WEEKEND)
  async updateDatabse(id: number, updateGithubJobDto: UpdateGithubJobDto) {
    return `This action updates a #${id} githubJob`;
  }
  
  // remove(id: number) {
  //   return `This action removes a #${id} githubJob`;
  // }

  findAll() {
    return `This action returns all githubJob`;
  }

  findOne(id: number) {
    return `This action returns a #${id} githubJob`;
  }
}

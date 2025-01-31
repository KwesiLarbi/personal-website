import { Test, TestingModule } from '@nestjs/testing';
import { GithubJobController } from './github-job.controller';
import { GithubJobService } from './github-job.service';

describe('GithubJobController', () => {
  let controller: GithubJobController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [GithubJobController],
      providers: [GithubJobService],
    }).compile();

    controller = module.get<GithubJobController>(GithubJobController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});

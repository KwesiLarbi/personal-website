import { Test, TestingModule } from '@nestjs/testing';
import { GithubJobService } from './github-job.service';

describe('GithubJobService', () => {
  let service: GithubJobService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [GithubJobService],
    }).compile();

    service = module.get<GithubJobService>(GithubJobService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
